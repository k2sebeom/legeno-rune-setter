from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton
from lcu_client import LCU_Client


app = QApplication([])

client = LCU_Client()

window = QWidget()
layout = QVBoxLayout()

label = QLabel('Welcome')
layout.addWidget(label)

status = QLabel('')
layout.addWidget(status)

button = QPushButton("Push")
layout.addWidget(button)

window.setLayout(layout)

window.show()

def on_connect(c):
    global label
    label.setText(f'Welcome {client.summoner_name}')

def on_champ_select(c, e):
    global status
    status.setText(f'Champion {client.current_champ.name} selected')

client.on_connect = on_connect
client.on_champ_select = on_champ_select

client.start()
app.exec()
