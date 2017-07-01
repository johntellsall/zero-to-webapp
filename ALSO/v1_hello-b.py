import os
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

# pick up port from Cloud9 environment
PORT_NUMBER = int(os.getenv('PORT', 8080))


def handle(handler):
	# Send the html message
	return "Hello World, woot!"
	

class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the HTTP GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write( handle(self) )

HTTPServer(('', PORT_NUMBER), myHandler).serve_forever()
	