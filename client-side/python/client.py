'''
    Author : GYZheng, http://github.com/iamgyz
    Feature : Client-side tool for update the Dynamic IP for the client
    Enviornment : Python3
    Update date : 2015.06.04
    In this project, I use my public MQTT Broker, you can use your own broker instead.
'''
from dipq_c import DIPQ_C

if __name__ == "__main__":
    host,port = 'gyzlab.com','1883'
    print('Please Enter your id, this is will be your own identifier')
    topic = input()
    dipq = DIPQ_C(host,port,topic)

