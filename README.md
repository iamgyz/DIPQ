# DIPQ
Dynamic IP Query system. For client side, run a small application to communicate with server. User can query dynamic IP by using server-side Restful-API.  

## Purpose  
For the hosts which are using dynamic IP and their home-gateway do not support ddns.

## Feature  
In client host, just run the application and enter your id, say 'qoo'. 
And the you can visit `http://<your-server-IP>:5566/qoo` to query your dynamic IP ANYWHERE!  


# Client-side

## Python version  

### Install  
1. `pip install paho-mqtt`  
2. `git clone https://github.com/iamgyz/DIPQ.git`  

### Usage
1. `cd client-side/python`  
2. `python3 client.py`  

## NodeJS version  

### Install  
1. `git clone https://github.com/iamgyz/DIPQ.git`  
2. `cd client-side/nodejs`  
3. `npm install`  

### Usage  
1. `npm start`  

# Server-side  

### Install  
1. `git clone https://github.com/iamgyz/DIPQ.git`  

### Usage
1. `cd server-side`  
2. `python3 server.py`  
Check `http://<your-server-IP>:5566` to check if the server is running well or not.  

# Live DEMO  
I've run a server application on my host http://gyzlab.com:5566  
So you can just clone client-side code and run it, and then you can query your real-time dynamic IP via http://gyzlab.com:5566/your-id
