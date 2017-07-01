"4_json.py: webserver, show raw JSON database"

import os
import http.server
import socketserver

DATA_PATH = 'data.json'

# pick up port from Cloud9 environment
PORT_NUMBER = int(os.getenv('PORT', 8080))

def get_data():
	with open(DATA_PATH) as data_file:
		data = data_file.read()
	return data

def safe_get_data():
	"if data file doesn't exist, create it with sample data"
	if not os.path.isfile(DATA_PATH):
		with open(DATA_PATH, 'w') as data_file:
			data_file.write('["beer", "tasty"]')
	return get_data()
	
def handle(handler):
	"Send the html message"
	data = safe_get_data()
	return "<h3>List of Internet Cats</h3> <HR> {}".format(data)
	

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
	