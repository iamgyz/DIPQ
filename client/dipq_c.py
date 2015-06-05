'''
    Author : GYZheng, http://github.com/iamgyz
    Feature : The library for Client-side Dynamic IP Query
    Enviornment : Python3
    Update date : 2015.06.04
'''
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import http.client
import time
from time import gmtime, strftime
#curl ipecho.net/plain
#curl gyzlab.com/myip/index.php
'''
100:Reg   -> 
          <-  150:Yes
          <-  180:No
          <-  200:Qry
300:<IP>  ->
'''
class DIPQ_C:
    def __init__(self,host,port,topic):
        self.host = host
        self.port = int(port)
        self.topic = topic
        self.subscribe_msg()

    def subscribe_msg(self):
        self.subscriber = mqtt.Client()
        self.subscriber.on_connect = self.on_connect
        self.subscriber.on_message = self.on_message
        self.is_connect = False #using this variable to wait for connect ready
        self.subscriber.connect(self.host,self.port);#keep_alive=60 
        #self.subscriber.loop_start()
        self.subscriber.loop_forever()
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
        #self.send_msg(self.nick_name+" is join the discussion\n")

    def on_message(self,client,userdata,msg):        
        message = msg.payload.decode('utf-8')
        if message == '200:Qry':
            print(self.time_log()+'Get new query request')
            ip = self.get_dynamic_ip()
            self.send_msg('300:'+ip);
            print(self.time_log()+'Publish Dynamic IP <'+ip+'>')
        #pass#print(msg.topic+" "+str(msg.payload))
    def get_dynamic_ip(self):
        conn = http.client.HTTPConnection("gyzlab.com")# or ipecho.net
        conn.request("GET", "/myip/index.php")#or /plain
        res = conn.getresponse()
        ip = res.read().decode('utf-8','ignore')
        return ip;
    def time_log(self):
        return '['+strftime("%Y-%m-%d %H:%M:%S", gmtime())+'] '
