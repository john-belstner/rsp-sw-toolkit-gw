#!/usr/bin/python

# This script implements a simple OSC client
# and sends a command.
#

import OSC

c = OSC.OSCClient()
c.connect(("127.0.0.1", 8585))   # connect to OSC server
oscmsg = OSC.OSCMessage()
oscmsg.setAddress("/pattern/2")
oscmsg.append("arrival")
c.send(oscmsg)
