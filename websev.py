'''
ifconfig en0






def createsocket():
    #the first argument will be the python file you are running, the arguements after will be the arguments you want to pass
    HOST = ''
    PORT = 

    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(1)
    server_ip = socket.gethostbyname(HOST)
    print server_ip
    print 'Serving HTTP on port %s ...' % PORT
    while True:
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(1024)
        print request
        #getRequest = "GET / HTTP/1.1\nHost:" +HOST+ "\n\n"
        if not request: 
            break
       # if request != accept:
            #need to check the accept to see if we are accepted to access the site
            #if we are than it is a 200 response

            #if we arent than it is a 501 response

            #if the client is not found than it is a 404 response
        http_response_200 = """\
        HTTP/1.1 200 OK

        read the file
        """
        http_response_501 = """\
        HTTP/1.1 501 OK

        Request method not implemented
        """
        http_response_404 = """\
        HTTP/1.1 404 NOT FOUND

        """
        client_connection.sendall(http_response_200)
        #client_connection.send(getRequest.encode())
        client_connection.close()

#socket_function()
'''

'''
def readFile():
    BASE_DIR = filename
    readFile = open(filename, 'r')
    print "Here's your file %r:" % filename
    readFile.read()
    print "reading the file"
    print readFile.read()
    readFile.close()
    return readFile
'''
def getFile():
    BASE_DIR = filename
    readFile = open(filename, 'r')
    print "Here's your file %r:" % filename
    readFile.read()
    print "reading the file"
    print readFile.read()
    readFile.close()
    return readFile


""" 
Makaila Akahoshi
CSC 546 Lab 04 - Building Web Services
Cody Buntain
first user enters site, the GET request is sent. 
it searches the server for the site and then return HTTP response

HTTP Server
using one of the major web browsers 
server should transmit any file requested by the browser
    may include HTML, CSS, Javascript
    use Version 1.1 via TCP
    support GET request method if not a GET return 501 ERROR
    support 200, 404, and 501 responses
    port 8080
"""
"first user enters site, the GET request is sent. it searches the server for the site and then return HTTP response"
