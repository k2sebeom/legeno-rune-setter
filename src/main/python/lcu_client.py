from lcu_driver import Connector
import json
import urllib.request as ur
from threading import Thread


class LCU_Client:
    def __init__(self):
        self.__runner = None
        champion_data = json.loads(ur.urlopen('http://ddragon.leagueoflegends.com/cdn/9.3.1/data/en_US/champion.json').read())['data']
        self.__champ_dict = dict()
        for champ in champion_data:
            c = champion_data[champ]
            self.__champ_dict[int(c['key'])] = champ.lower()

        map_data = json.loads(ur.urlopen('https://static.developer.riotgames.com/docs/lol/maps.json').read())
        self.__map_dict = dict()
        for m in map_data:
            map_name = m['mapName']
            if 'Abyss' in map_name:
                self.__map_dict[m['mapId']] = 'aram'
            else:
                self.__map_dict[m['mapId']] = 'rift'

        self.conn = Connector()

        self.summoner_id = 0
        self.summoner_name = ""
        self.current_champ_id = 0
        self.current_champ_name = ""
        self.current_game_mode = ""

        self.on_connect = lambda c: None
        self.on_champ_select = lambda c, e: None
        self.on_close = lambda c: None

        @self.conn.ready
        async def connected(connection):
            summoner = await connection.request('get', '/lol-summoner/v1/current-summoner')
            data = await summoner.json()
            self.summoner_name = data['displayName']
            self.summoner_id = data['summonerId']
            self.on_connect(connection)

        @self.conn.ws.register('/lol-champ-select/v1/session', event_types=('UPDATE',))
        async def selected(connection, event):
            data = event.data
            team = data['myTeam']
            for player in team:
                if player['summonerId'] == self.summoner_id:
                    if player['championId'] != self.current_champ_id:
                        self.current_champ_id = player['championId']
                        self.current_champ_name = self.__champ_dict.get(self.current_champ_id, 'Unknown')
                        gameflow = await connection.request('get', '/lol-gameflow/v1/session')
                        gameflow_data = await gameflow.json()
                        map_id = gameflow_data['gameData']['queue']['mapId']
                        self.current_game_mode = self.__map_dict.get(map_id, 'rift')
                        self.on_champ_select(connection, event)
                    break

        @self.conn.close
        async def disconnected(connection):
            await self.conn.stop()
            self.on_close(connection)

    def start(self):
        self.__runner = Thread(target=self.__run_connection, daemon=True)
        self.__runner.start()

    def __run_connection(self):
        self.conn.start()
