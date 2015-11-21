import socket

host = ''  
port = 8080
#first needs to set up the socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

Resource
http://python.about.com/od/networkingwithpython/ss/PythonWebServer.htm#step6

<variable> = socket.socket(<family>, <type>)
'''
The recognised socket families are:

AF_INET: IPv4 protocols (both TCP and UDP)
AF_INET6: IPv6 protocols (both TCP and UDP)
AF_UNIX: UNIX domain protocols
The first two are obviously internet protocols. Anything that travels over the internet can be accessed in these families. Many networks still do not run on IPv6. So, unless you know otherwise, it is safest to default to IPv4 and use AF_INET.
The socket type refers to the type of communication used through the socket. The five socket types are as follows:

SOCK_STREAM: a connection-oriented, TCP byte stream
SOCK_DGRAM: UDP transferral of datagrams (self-contained IP packets that do not rely on client-server confirmation)
SOCK_RAW: a raw socket
SOCK_RDM: for reliable datagrams
SOCK_SEQPACKET: sequential transfer of records over a connection
'''