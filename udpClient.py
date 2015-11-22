#!/usr/bin/python
import argparse
from socket import *
def udp_client(args):
	serverName = "255.255.255.255"
	serverPort = args.serverPort

	clientSocket = socket(AF_INET, SOCK_DGRAM)
	clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
	while 1:
		message = raw_input("Enter your message:")
		clientSocket.sendto(message,(serverName, serverPort))	
		if message == 'exit':
			print'The client is exiting...'
			clientSocket.close()
			break
		else:
			newmessage, serverAddress = clientSocket.recvfrom(1024)
			print "Started communication with: ", serverAddress[0]
			print newmessage
			if newmessage == 'exit':
				print 'The server wants to stop communication'
				break
	print 'closing the socket...'
	clientSocket.close()
	print 'communication has ended'

def main():
    parser = argparse.ArgumentParser(prog='UDPServer', description='Create a chat service') 
    #these are optional since the program should run without the inputs
    parser.add_argument('-p','--port=####', dest= 'serverPort', default = 8080, type = int, action='store', help='PORT Port number to listen on')
    #8081 1024-65000 for testing the port
    args = parser.parse_args()
    print args
    #if you receive an argument for the port from the command line
    if args.serverPort != None:
        #make port = to the argument
        udp_client(args)

if __name__ == "__main__":
    main()   