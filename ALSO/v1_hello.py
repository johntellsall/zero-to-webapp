import os
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = int(os.getenv('PORT', 8080))

class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write("Hello World !")
		return

HTTPServer(('', PORT_NUMBER), myHandler).serve_forever()
	