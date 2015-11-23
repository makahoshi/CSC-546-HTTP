         domain = url.split('/')
         print domain[1]
         finalurl = domain[1]
         requesttype = mimetypes.guess_type(finalurl)
         print requesttype
         reqtype = str(requesttype[0])
         print reqtype

                     #req = urllib2.Request(url,None, header)
            #response = urllib2.urlopen(req)
            #response = urllib2.urlopen('http://localhost:8080/')
         #headers = { 'User-Agent' : user_agent }