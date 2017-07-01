"3_block.py: webserver, show HTML from file"

import os
import http.server
import socketserver


# pick up port from Cloud9 environment
PORT_NUMBER = int(os.getenv('PORT', 8080))

def get_html():
	with open('data.html') as data_file:
		html = data_file.read()
	return html
	
def handle(handler):
	"Send the html message"
	html = get_html()
	return "Hello World, woot! <HR> {}".format(html)
	

class MyHandler(http.server.SimpleHTTPRequestHandler):
	
	#Handler for the HTTP GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		return_str = handle(self)
		return_bytes = return_str.encode('utf-8')
		self.wfile.write( return_bytes )

webserver = socketserver.TCPServer(("", PORT_NUMBER), MyHandler)
webserver.serve_forever()
	