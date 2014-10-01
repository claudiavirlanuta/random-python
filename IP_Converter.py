"""
import socket
if hasattr(socket, 'setdefaulttimeout'):
    # Set the default timeout on sockets to 5 seconds
    socket.setdefaulttimeout(5)
 socket.gethostbyaddr("69.59.196.211")
('stackoverflow.com', ['211.196.59.69.in-addr.arpa'], ['69.59.196.211'])
"""
import socket
file = 'C:\Users\claudia.virlanuta\Documents\TechTarget_IPs.txt'
f = open(file, 'r')
lines = f.readlines()
f.close()
output = open('C:\Users\claudia.virlanuta\Documents\TechTarget_Domains.txt', 'w')
for i in lines:
    host = i.strip()
    output.write("%s - %s\n" % (host, socket.getfqdn(host)))