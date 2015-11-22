#!/usr/bin/python
import argparse
from socket import *

def udp_server(args):

	serverPort = args.serverPort
	serverSocket = socket(AF_INET, SOCK_DGRAM) 
	serverSocket.bind(('', serverPort))
	#clientSocket.setsocket(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	print "The server is ready to receive"

	while 1:
		#receiving messages
		message, clientAddress = serverSocket.recvfrom(1024) 
		print "Started communication with:", clientAddress[0]
		#print 'Message from %s: %s'%(clientAddress[0], message)
		print message
		if message == 'exit':
			print 'The client wants to stop communication'
			break
		else:
			#they still want to communicate enter message
			newmessage = raw_input("Enter your message: ")
			#sending the message 
			serverSocket.sendto(newmessage, clientAddress)
			if newmessage == 'exit':
				print 'The server wants to stop communication'
				break
	serverSocket.close()
	print 'The server has closed'

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
        udp_server(args)
if __name__ == "__main__":
    main()   