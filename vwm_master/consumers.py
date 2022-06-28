
import json
from channels.generic.websocket import WebsocketConsumer
import json
from time import sleep
import serial
from random import randint
class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        # ser=serial.Serial(port='COM1', timeout=.1)
        # ser.baudrate=9600
        # ser.bytesize=serial.EIGHTBITS
        # ser.parity= serial.PARITY_NONE
        # ser.stopbits= serial.STOPBITS_ONE
        sign=""

        for i in range(1000):
            weight=randint(1, 100)
            

        # while(1):
        #     if not ser.isOpen():
        #         ser.open()

        #     asc=ser.read(96).hex()
        #     for i in range(len(asc)):
        #         if asc[i]=='2':
        #             if asc[i+1]=='b':
        #                 i+=1
        #                 break
        #             elif asc[i+1]=='d':
        #                 sign="-"
        #                 i+=1
        #                 break
        #     try:
        #         weight=int(asc[i+2:i+14:2])
        #     except:
        #         weight= "Invalid"
            self.send(json.dumps({
                "weight": weight,
                "sign": sign
            }))
            sleep(1)


