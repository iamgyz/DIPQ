/*
    Author : GYZheng, http://github.com/iamgyz
    Feature : Client-side tool for update the Dynamic IP for the client
    Enviornment : nodejs
    Update date : 2015.06.11
    In this project, I use my public MQTT Broker, you can use your own broker instead.
*/
var mqtt    = require('mqtt');
var http = require('http');
var prompt = require('prompt');
var fetch = require('node-fetch');

var DIPQ = function(host,port,topic){
    this.host = host;
    this.port = port;
    this.topic = topic;
    this.run = function(){
        var client =  mqtt.connect({ host: this.host, port: this.port });
        client.on('connect',function(){            
            console.log(this.getTime()+"Connected to broker");
            client.subscribe(this.topic);
        }.bind(this));//記得要把this的scope傳給callback
        client.on('message',function(topic,message){
            var that = this;
            msg = message.toString();
            if(msg == '200:Qry'){
                console.log(this.getTime()+"Get new request");
                //get my dynamic ip
                fetch('http://gyzlab.com/myip/index.php')
                .then(function(res){
                    return res.text();
                })
                .then(function(body){
                    var _msg = '300:'+body;
                    client.publish(that.topic,_msg,function(){
                        console.log(that.getTime()+"Publish IP <"+body+">");
                    });   
                });
            }
        }.bind(this));
	
    };
    //utilities
    this.getTime = function(){
        return '['+new Date().toString()+'] ';
    };
};

/*
    Main part, you can change the broker address to your own broker for private useage    
*/
prompt.message = 'Please Enter your id, which will be your own identifier';
prompt.start();
prompt.get('id',function (err, result) {
   var dipq = new DIPQ('gyzlab.com',1883,result.id);
   dipq.run();
});
