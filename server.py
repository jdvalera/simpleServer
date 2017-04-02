#!/usr/bin/env python
 
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
 
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
port = 8000
server_address = ("", 8000)
handler.cgi_directories = ["/"]
 
httpd = server(server_address, handler)
print "Starting server..."
httpd.serve_forever()
