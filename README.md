# DIPQ
Dynamic IP Query system. For client side, run a small application to communicate with server. User can query dynamic IP by using server-side Restful-API

### Depency  
paho-mqtt

### Install  
`git clone https://github.com/iamgyz/DIPQ.git`  
`pip install paho-mqtt`  

#### Client-side  
`cd client`  
`python3 client.py`  

#### Server-side  
`cd server`  
`python3 server.py`  

Check http://localhost:5566 to check if the server is running well or not.  

### Usage  
In client host, just run the application and enter your id, say 'qoo' 
And the you can visit http://<server IP>:5566/qoo to query your dynamic IP ANYWHERE!  

### Live DEMO  
I've run a server application on my host http://gyzlab.com:5566  
So you can just clone client-side code and run it, and then you can query your real-time dynamic IP via http://gyzlab.com:5566/your-id
