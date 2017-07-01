import os
# 2.7: from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import http.server
import socketserver


# pick up port from Cloud9 environment
PORT_NUMBER = int(os.getenv('PORT', 8080))


def handle(handler):
	# Send the html message
	return "Hello World, woot!"
	

class MyHandler(http.server.SimpleHTTPRequestHandler):
	
	#Handler for the HTTP GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		return_str = handle(self)
		return_bytes = return_str.encode('utf-8')
		self.wfile.write( return_bytes )

# 2.7: HTTPServer(('', PORT_NUMBER), myHandler).serve_forever()
webserver = socketserver.TCPServer(("", PORT_NUMBER), MyHandler)
webserver.serve_forever()
	