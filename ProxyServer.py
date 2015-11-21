#first import some libraries
import socket
import sys
import argparse
import path
import os
import BaseHTTP
import urllib
import urllib2
#are encouraged to use urllib2
#first get arguments from the user 
print '\nNumber of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv), '\n'
def socket_function(args):
	HOST, PORT = '', 8080

	listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	listen_socket.bind((HOST, PORT))
	listen_socket.listen(1)
	print 'Serving HTTP on port %s ...' % PORT
	while True:
	    client_connection, client_address = listen_socket.accept()
	    request = client_connection.recv(1024)
	    print request
	    url = ''
	    #this is where we use urllib2
	    req = urllib2.Request('http://www.voidspace.org.uk')
	    #req = urllib2.Request(url,None, header)
		response = urllib2.urlopen(req)
		website = response.read()
		headers = { 'User-Agent' : user_agent }
		try: 
			urllib2.urlopen(req)
			print "This is the response info:", response.info()
			print "This is the URL:", response.geturl()
		except urllib2.HTTPError as e:
			print 'Error Code:', e.code
			print e.read()
			print BaseHTTPServer.BaseHTTPRequestHandler.responses
	    except urllib2.URLError as e:
		    print 'We failed to reach a server.'
		    print 'Reason: ', e.reason
	    
	    http_response = """\
		HTTP/1.1 200 OK

		index.html
		"""
	    client_connection.sendall(website)
	    client_connection.close()

def main():
    parser = argparse.ArgumentParser(prog='WebServer', description='Create a web server that will be able to display an HTML file') 
    #these are optional since the program should run without the inputs
    parser.add_argument('-p','--port=####', dest= 'PORT', default = 8080, type = int, action='store', help='PORT Port number to listen on')
    #8081 1024-65000 for testing the port
    parser.add_argument('-f','--fun', dest= 'url', type = str, action='store', help='for something fun')

    args = parser.parse_args()
    print args
    #if you receive an argument for the port from the command line
    if args.PORT != None:
        #make port = to the argument
        socket_function(args)
        print PORT
 	if args.url != None:
 		socket_function(args)
 		print url
if __name__ == "__main__":
    main()   