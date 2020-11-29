#!/usr/bin/python

# This script implements a simple OSC server
# that looks for four simple address atterns.
#

from OSC import OSCServer,OSCClient, OSCMessage
from time import sleep
import types

def L1(action):
    print(action, "D11","L1")

def L2(action):
    print(action, "D11","L2")
    
def L3(action):
    print(action, "D11","L3")
    
def L4(action):
    print(action, "D11","L4")
        

server = OSCServer(("127.0.0.1", 8585))

def push1_callback(path, tags, args, source):
    if path=="/pattern/1":
        L1(args[0])

def push2_callback(path, tags, args, source):
    if path=="/pattern/2":
        L2(args[0])

def push3_callback(path, tags, args, source):
    if path=="/pattern/3":
        L3(args[0])

def push4_callback(path, tags, args, source):
    if path=="/pattern/4":
        L4(args[0])

def handle_error(self,request,client_address):
    pass

server.addMsgHandler( "/pattern/1",push1_callback)
server.addMsgHandler( "/pattern/2",push2_callback)
server.addMsgHandler( "/pattern/3",push3_callback)
server.addMsgHandler( "/pattern/4",push4_callback)


server.handle_error = types.MethodType(handle_error, server)

while True:
	server.handle_request()

server.close()