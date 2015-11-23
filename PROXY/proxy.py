#first import some libraries
import socket
import sys
import argparse
import path
import os
import urllib
import urllib2
import mimetypes
#first get arguments from the user
print '\nNumber of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv), '\n'
def socket_function(args):
   HOST = ''
   PORT = args.PORT
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
         getrequest = request.split( )
         #print getrequest
         url = getrequest[1]
         urlfun = args.urlfun
         if urlfun != None:	
            try:
               req = urllib2.Request(urlfun)
               response = urllib2.urlopen(req)
               print '\n<---------------------------------------->'
               print "This is the GET request"
               print 'RESPONSE:', response
               print 'URL     :', response.geturl()
               headers = response.info()
               content = headers['Content-Type']
               response_code = response.code
               print 'CONTENT-TYPE :', content
               print 'HEADERS :', headers
               print "This gets the code: ", response.code
               print '<------------------------------------------\n>'
               if response_code == 200:
                  website = response.read()
                  length = len(website)
                  http200 = "HTTP/1.1 200 OK"
                  response = http200+"\n"+content+"\n\n"+str(website)
                  client_connection.sendall(response)
                  client_connection.close()
               if response_code == 404:
                  http404 = "HTTP/1.1 404 NOT Found"
                  print http404
                  response = http404+"\n"+content+"\n\n"+"404 NOT FOUND"
                  client_connection.sendall(response)
                  client_connection.close()
               if response_code == 501:
                  http501 = "HTTP/1.1 501 Request method not implemented"
                  response = http501+"\n"+content_type+"\n\n"+"501 Request method not implemented"
                  client_connection.sendall(response)
                  client_connection.close()
            except urllib2.HTTPError as e:
              print 'Error Code:', e.code
              print e.read()
              if e.code == 404:
                  req = urllib2.Request(url)
                  response = urllib2.urlopen(req)
                  headers = response.info()
                  content = headers['Content-Type']
                  http404 = "HTTP/1.1 404 NOT Found"
                  response = http404+"\n"+content+"\n\n"+"404 NOT FOUND"
                  client_connection.sendall(response)
                  client_connection.close()
         else:
            try:
               req = urllib2.Request(url)
               response = urllib2.urlopen(req)
               print '\n<---------------------------------------->'
               print "This is the GET request"
               print 'RESPONSE:', response
               print 'URL     :', response.geturl()
               headers = response.info()
               content = headers['Content-Type']
               response_code = response.code
               print 'CONTENT-TYPE :', content
               print 'HEADERS :', headers
               print "This gets the code: ", response.code
               print '<------------------------------------------\n>'
               if response_code == 200:
                  website = response.read()
                  length = len(website)
                  http200 = "HTTP/1.1 200 OK"
                  response = http200+"\n"+content+"\n\n"+str(website)
                  client_connection.sendall(response)
                  client_connection.close()
               if response_code == 404:
                  http404 = "HTTP/1.1 404 NOT Found"
                  print http404
                  response = http404+"\n"+content+"\n\n"+"404 NOT FOUND"
                  client_connection.sendall(response)
                  client_connection.close()
               if response_code == 501:
                  http501 = "HTTP/1.1 501 Request method not implemented"
                  response = http501+"\n"+content_type+"\n\n"+"501 Request method not implemented"
                  client_connection.sendall(response)
                  client_connection.close()
            except urllib2.HTTPError as e:
               print 'Error Code:', e.code
               print e.read()
               if e.code == 404:
                  req = urllib2.Request(url)
                  response = urllib2.urlopen(req)
                  headers = response.info()
                  content = headers['Content-Type']
                  http404 = "HTTP/1.1 404 NOT Found"
                  response = http404+"\n"+content+"\n\n"+"404 NOT FOUND"
                  client_connection.sendall(response)
                  client_connection.close()
      else:
         print "This is not a GET request" #then this is a 501 error
	 print "---------------------------------------------------------------"

def main():
    parser = argparse.ArgumentParser(prog='WebServer', description='Create a web server that will be able to display an HTML file')
    #these are optional since the program should run without the inputs
    parser.add_argument('-p','--port=####', dest= 'PORT', default = 8080, type = int, action='store', help='PORT Port number to listen on')
    #8081 1024-65000 for testing the port
    parser.add_argument('-f','--fun', dest= 'urlfun', type = str, action='store', help='for something fun')
    args = parser.parse_args()
    print args
    #if you receive an argument for the port from the command line
    if args.PORT != None:
       #make port = to the argument
       socket_function(args)
    if args.urlfun != None:
       socket_function(args)
if __name__ == "__main__":
    main()
