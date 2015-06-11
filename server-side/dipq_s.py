'''
    Author : GYZheng, http://github.com/iamgyz
    Feature : The library for Server-side Dynamic IP Query
    Enviornment : Python3
    Update date : 2015.06.04
'''
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import http.client
import time
from time import gmtime, strftime

class DIPQ_S:#DIPQ_SERVER
    def __init__(self,host,port,topic):
        self.host = host
        self.port = int(port)
        self.topic = topic
        self.ip = 'None'#result ip
        self.subscribe_msg()
    def subscribe_msg(self):
        self.subscriber = mqtt.Client()
        self.subscriber.on_connect = self.on_connect
        self.subscriber.on_message = self.on_message
        self.is_connect = False #using this variable to wait for connect ready
        self.subscriber.connect(self.host,self.port);#keep_alive=60 
        self.subscriber.loop_start()
        #self.subscriber.loop_forever()
        #waiting for connection to be built
        while self.is_connect == False:
            pass#donothig...

    def send_msg(self,msg):
        #msg = "["+self.nick_name + "] : "+msg
        publish.single(self.topic,msg, hostname=self.host, port=self.port)

    def on_connect(self,client, userdata, flags, rc):
        #print("Connected with result code "+str(rc))
        self.is_connect = True
        client.subscribe(self.topic)
        print(self.time_log()+"Connected! ")
        print(self.time_log()+"Send new query request")
        self.send_msg('200:Qry');
        #self.send_msg(self.nick_name+" is join the discussion\n")

    def on_message(self,client,userdata,msg):        
        message = msg.payload.decode('utf-8')
        if message.startswith('300:'):
            print(self.time_log()+'Get query result')
            self.ip = message.split(':')[1]
            print(self.time_log()+'Dynamic IP is <'+self.ip+'>')
            self.is_connect = False;
    def time_log(self):
        return '['+strftime("%Y-%m-%d %H:%M:%S", gmtime())+'] '

    def wait_result(self):
        count = 0
        limit = 20 # Around 20 seconds
        while self.is_connect == True:
            time.sleep(1)#sleep for 1 s
            count = count + 1
            if count > 30:
                break
        #After break the while
        return self.ip

