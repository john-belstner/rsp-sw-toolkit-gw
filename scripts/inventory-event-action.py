#!/usr/bin/python

# This script is called by the UpstreamManager
# everytime an upstream inventory event is sent.
#
# The arguments passed are...
# $1 = EPC (a bunch of hex characters)
# $2 = Event (none, arrival, moved, departed, returned, cycle_count)
# $3 = Location (RSP-xxxxxx, where xxxxxx are the last 3 octets of the RSP MAC address)

import sys

# Check for three arguements
if (len(sys.argv) != 4):
    print("")
    print("USAGE: python inventory-event-action.py <epc> <event> <location>")
    print("")
    sys.exit(1)

# comp_index = int(sys.argv[1])
SL_OSC_IP_ADDRESS="127.0.0.1"
SL_OSC_INPUT_PORT=8585

EPC      = sys.argv[1]
EVENT    = sys.argv[2]
LOCATION = sys.argv[3]

EPC1 = "100683590000000000000700"
EPC2 = "100683590000000000000701"
EPC3 = "100683590000000000000702"
EPC4 = "100683590000000000000703"


file = open("event-list.txt","a+")
file.write("EPC = " + EPC + "  EVENT = " + EVENT + "  LOCATION = " + LOCATION + "\n")
file.close()


def send_osc_pattern1_py3():
    client = udp_client.SimpleUDPClient(SL_OSC_IP_ADDRESS, SL_OSC_INPUT_PORT)
    client.send_message("/pattern/1", 1)

def send_osc_pattern2_py3():
    client = udp_client.SimpleUDPClient(SL_OSC_IP_ADDRESS, SL_OSC_INPUT_PORT)
    client.send_message("/pattern/2", 1)

def send_osc_pattern3_py3():
    client = udp_client.SimpleUDPClient(SL_OSC_IP_ADDRESS, SL_OSC_INPUT_PORT)
    client.send_message("/pattern/3", 1)

def send_osc_pattern4_py3():
    client = udp_client.SimpleUDPClient(SL_OSC_IP_ADDRESS, SL_OSC_INPUT_PORT)
    client.send_message("/pattern/4", 1)



def send_osc_pattern_1_py2(ip_address=SL_OSC_IP_ADDRESS, osc_port=SL_OSC_INPUT_PORT, osc_address="/pattern/1"):
    c = OSC.OSCClient()
    c.connect((ip_address, osc_port))
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress(osc_address)
    oscmsg.append(EVENT)
    c.send(oscmsg)

def send_osc_pattern_2_py2(ip_address=SL_OSC_IP_ADDRESS, osc_port=SL_OSC_INPUT_PORT, osc_address="/pattern/2"):
    c = OSC.OSCClient()
    c.connect((ip_address, osc_port))
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress(osc_address)
    oscmsg.append(EVENT)
    c.send(oscmsg)

def send_osc_pattern_3_py2(ip_address=SL_OSC_IP_ADDRESS, osc_port=SL_OSC_INPUT_PORT, osc_address="/pattern/3"):
    c = OSC.OSCClient()
    c.connect((ip_address, osc_port))
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress(osc_address)
    oscmsg.append(EVENT)
    c.send(oscmsg)

def send_osc_pattern_4_py2(ip_address=SL_OSC_IP_ADDRESS, osc_port=SL_OSC_INPUT_PORT, osc_address="/pattern/4"):
    c = OSC.OSCClient()
    c.connect((ip_address, osc_port))
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress(osc_address)
    oscmsg.append(EVENT)
    c.send(oscmsg)


if sys.version_info[0] < 3:
    print("python2 osc initalized")
    import OSC
    if EPC==EPC1:
        send_osc_pattern_1_py2()
    elif EPC==EPC2:
        send_osc_pattern_2_py2()
    elif EPC==EPC3:
        send_osc_pattern_3_py2()
    else:
        send_osc_pattern_4_py2()
else:
    print("python 3 osc initalized")
    from pythonosc import udp_client
    if EPC==EPC1:
        send_osc_pattern1_py3()
    elif EPC==EPC2:
        send_osc_pattern2_py3()
    elif EPC==EPC3:
        send_osc_pattern3_py3()
    else:
        send_osc_pattern4_py3()


sys.exit(0)