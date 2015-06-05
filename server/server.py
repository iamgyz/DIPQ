'''
    Author : GYZheng, http://github.com/iamgyz
    Feature : Provide API for query Dynamic IP
    Enviornment : Python3
    Update date : 2015.06.04
    In this project, I use my public MQTT Broker, you can use your own broker instead.
    The API will run @port 5566, you can also modify by yourself.
'''
from dipq_s import DIPQ_S
from flask import Flask
from flask.ext.cors import cross_origin

app = Flask(__name__)
@app.route('/')
def index():
    return 'This is the index page of API'

@app.route('/<userid>')
@cross_origin() # allow all origins all methods.
def search(userid):
    host,port = 'gyzlab.com','1883'
    dipq_s = DIPQ_S(host,port,userid)
    result = dipq_s.wait_result()
    print(dipq_s.time_log()+"Return result "+result)
    return result

if __name__ == '__main__': 
    app.run(host='0.0.0.0',port=5566,threaded=True)

