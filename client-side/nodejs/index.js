/*
    Author : GYZheng, http://github.com/iamgyz
    Feature : Client-side tool for update the Dynamic IP for the client
    Enviornment : nodejs
    Update date : 2015.06.11
    In this project, I use my public MQTT Broker, you can use your own broker instead.
*/
var mqtt    = require('mqtt');
var http = require('http');

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
            msg = message.toString();
            if(msg == '200:Qry'){
                console.log(this.getTime()+"Get new request");
                //get my dynamic ip
                http.get({host:'gyzlab.com',path:'/myip/index.php'},function(res){
                    var body='';
                    res.on('data',function(d){
                        body+=d;
                    });
                    res.on('end',function(){            
                        var msg = '300:'+body
                        client.publish(this.topic,msg,function(){
                            console.log(this.getTime()+"Publish IP <"+body+">");
                        }.bind(this));
                    }.bind(this));
                }.bind(this));    
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
var dipq = new DIPQ('gyzlab.com',1883,"topic");
dipq.run();
