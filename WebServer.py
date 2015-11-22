#first import some libraries
import socket
import sys
import argparse
import path
import os
#import m2crypto
import mimetypes
import time
import datetime

from OpenSSL import SSL
#http://carlo-hamalainen.net/blog/2013/1/24/python-ssl-socket-echo-test-with-self-signed-certificate
#first get arguments from the user 
#http://the.randomengineer.com/2014/01/29/using-ssl-wrap_socket-for-secure-sockets-in-python/
#http://bobthegnome.blogspot.com/2007/08/making-ssl-connection-in-python.html
#for SSL I downloaded and installed https://github.com/pyca/pyopenssl
#so to run my code I used Annaconda, which I had pyopenssl installed
#https://github.com/openssl/openssl/blob/master/INSTALL
print '\nNumber of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv), '\n'
def socket_function(args):
    HOST = ''
    PORT = args.PORT
    BASE_DIR = args.BASE_DIR
    #context = SSL.Context(SSL.SSLv23_METHOD)
    #context.use_privatekey_file('key')
    #context.use_certificate_file('cert')
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #listen_socket = SSL.Connection(context, listen_socket)
    listen_socket.bind((HOST, PORT))
    #sslSocket = socket.ssl(listen_socket)
    listen_socket.listen(1)
    server_ip = socket.gethostbyname(HOST)
    print "This is the server IP" + server_ip
    print 'Serving HTTP on port %s ...' % PORT
    while True:
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(1024)
        print request
        requestPreface = request[:3] #this gives you the preface of the get of it is a get
        if requestPreface == 'GET':
            print requestPreface
            getrequest = request.split( )
            print getrequest
            newrequest = getrequest[1]
            requesttype = mimetypes.guess_type(newrequest)
            reqtype = str(requesttype[0])
            print "this is the type of my request", requesttype[0]
            print newrequest
            #now we have to account for the 202, 404, and 501
            try:
                File = open(BASE_DIR+newrequest, 'rb') #rb
                print "Here's your file %r:" % BASE_DIR+newrequest
                readFile = File.read()
                File.close()
                #GET /path/to/file/index.html HTTP/1.0
                '''HTTP/1.1 200 OK
                Date: Fri, 31 Dec 1999 23:59:59 GMT
                Content-Type: text/plain
                Content-Length: 42
                some-footer: some-value
                another-footer: another-value'''

                http200 = "HTTP/1.1 200 OK"
                content_type = "Content-Type: %s" %reqtype
                now = time.strftime("%c")
                now1 = datetime.datetime.now()
                date = now1
                print date
                response = http200+"\n"+content_type+"\n\n"+readFile
                #print response
                client_connection.sendall(response)
                client_connection.close()
            except IOError as e:
                print('Uh oh! the file does not exist')
                http404 = "HTTP/1.1 404 Not Found"
                content_type = "Content-Type: %s" %reqtype
                response = http404+"\n"+content_type+"\n\n"+"404 NOT FOUND"
                #print response
                client_connection.send(response)
                client_connection.close()
        if requestPreface != 'GET':
            print "this is not a GET request" #then this is a 501 error
            print "501 ERROR"
            http501 = "HTTP/1.1 501 Request method not implemented"
            content_type = "Content-Type: %s" %reqtype
            response = http501+"\n"+content_type+"\n\n"+"501 Request method not implemented"
            #when post and head are sent  
            client_connection.sendall(http501)
            client_connection.close()   
def main():
    parser = argparse.ArgumentParser(prog='WebServer', description='Create a web server that will be able to display an HTML file') 
    #these are optional since the program should run without the inputs
    parser.add_argument('-p','--port=####', dest= 'PORT', default = 8080, type = int, action='store', help='PORT Port number to listen on')
    #8081 1024-65000 for testing the port
    parser.add_argument('-b','--base=/path/to/directory', dest = 'BASE_DIR', default = "/Users/makahoshi/Desktop/CSC_546_HTTP/example_site-2" ,type = str, action='store', help='BASE_DIR Base dir containing website')
    args = parser.parse_args()
    print args
    #if you receive an argument for the port from the command line
    if args.PORT != None:
        #make port = to the argument
        socket_function(args)
        print PORT
    if args.BASE_DIR != None:
        socket_function(args)
        print BASE_DIR

if __name__ == "__main__":
    main()   