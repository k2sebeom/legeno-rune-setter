from lcu_driver import Connector
import json
import urllib.request as ur
from threading import Thread


class Champion:
    def __init__(self, champ_id, alias, name):
        self.champ_id = champ_id
        self.alias = alias
        self.name = name


class GameMap:
    def __init__(self, map_id, name, game_mode):
        self.map_id = map_id
        self.name = name
        self.mode = game_mode


class LCU_Client:
    def __init__(self):
        self.__runner = None
        self.connection = None
        self.conn = Connector()

        self.summoner_id = 0
        self.summoner_name = ""
        self.current_champ = Champion(-1, "", "")
        self.current_map = GameMap(-1, "", "")

        self.__champ_dict = dict()
        self.__map_dict = dict()

        self.on_connect = lambda c: None
        self.on_champ_select = lambda c, e: None
        self.on_close = lambda c: None

        @self.conn.ready
        async def connected(connection):
            self.connection = connection
            summoner = await connection.request('get', '/lol-summoner/v1/current-summoner')
            data = await summoner.json()
            self.summoner_name = data['displayName']
            self.summoner_id = data['summonerId']
            self.on_connect(connection)

            champions = await self.connection.request('get', f'/lol-champions/v1/inventories/{self.summoner_id}/champions')
            self.__champ_dict = await champions.json()
            maps = await self.connection.request('get', '/lol-maps/v1/maps')
            self.__map_dict = await maps.json()

        @self.conn.ws.register('/lol-champ-select/v1/session', event_types=('UPDATE',))
        async def selected(connection, event):
            data = event.data
            team = data['myTeam']
            for player in team:
                if player['summonerId'] == self.summoner_id:
                    if player['championId'] != self.current_champ.champ_id:
                        await self._set_champion(player['championId'])
                        gameflow = await connection.request('get', '/lol-gameflow/v1/session')
                        gameflow_data = await gameflow.json()
                        map_id = gameflow_data['gameData']['queue']['mapId']
                        for m in self.__map_dict:
                            if m['id'] == map_id:
                                self.current_map = GameMap(m['id'], m['name'], m['gameMode'])
                                break
                        self.on_champ_select(connection, event)
                    break

        @self.conn.close
        async def disconnected(connection):
            await self.conn.stop()
            self.on_close(connection)

    async def _set_champion(self, champ_id):
        for c in self.__champ_dict:
            if c['id'] == champ_id:
                self.current_champ = Champion(c['id'], c['alias'], c['name'])
                break

    def start(self):
        self.__runner = Thread(target=self.__run_connection, daemon=True)
        self.__runner.start()

    def __run_connection(self):
        self.conn.start()
