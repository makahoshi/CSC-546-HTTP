#first import some libraries
import socket
import sys
import argparse
import path
import os
import urllib
import urllib2
import mimetypes
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
        requestPreface = request[:3] #this gives you the preface of the get of it is a get
        if requestPreface == 'GET':
            #req = urllib2.Request(url,None, header)
            #url = 'http://localhost:8080/'
            getrequest = request.split( )
            print getrequest
            url = getrequest[1]
            domain = url.split('/')
            print domain[1]
            finalurl = domain[1]
            requesttype = mimetypes.guess_type(finalurl)
            print requesttype
            reqtype = str(requesttype[0])
            print reqtype
            req = urllib2.Request('http://'+finalurl)
            response = urllib2.urlopen(req)
            print '----------------------------------------'
            print 'RESPONSE:', response
            print 'URL     :', response.geturl()
            headers = response.info()
            date = headers['date']
            content = headers['Content-Type']
            response_code = response.code
            print 'DATE    :', date
            print 'CONTENT-TYPE :', content
            print '------------------------------------------'
            print 'HEADERS :', headers
            print "This gets the code: ", response.code
            #req = urllib2.Request(url,None, header)
            #response = urllib2.urlopen(req)
            #response = urllib2.urlopen('http://localhost:8080/')
			#headers = { 'User-Agent' : user_agent }
            try:
                if response_code == 200:
	                website = response.read()
	                length = len(website)
	                #print website
	                http200 = "HTTP/1.1 200 OK"
	                response = http200+"\n"+str(headers)+"\n\n"+str(website)
	                client_connection.sendall(response)
	                client_connection.close()
                if response_code == 404:
                    print 'error 404'
                if response_code == 501:
	           		print 'error 501'
            except urllib2.HTTPError as e:
                print 'Error Code:', e.code
                print e.read()
            except urllib2.URLError as e:
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
	                #print response
	               #client_connection.sendall(response)
	if requestPreface != 'GET':
            print "this is not a GET request" #then this is a 501 error
            print "501 ERROR"

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
