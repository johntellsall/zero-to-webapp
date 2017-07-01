'''
webapp v6: use data from JSON file; prefill if needed
'''

import json
import os
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

# pick up port from Cloud9 environment
PORT_NUMBER = int(os.getenv('PORT', 8080))

# enable Bootstrap; see http://getbootstrap.com/getting-started/
BOOTSTRAP_HEADER_HTML = '''
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
'''

FORM_HTML = '''
<form method="POST">
<input name="label">
<input type="submit">
</form>
'''

DATA_PATH = 'mylist.json'

def get_list():
	return json.load(open(DATA_PATH))

def safe_get_list():
	'get list of data; prefill with sample data if file missing'
	if not os.path.isfile(DATA_PATH):
		with open(DATA_PATH, 'w') as out_file:
			json.dump(['porcine', 'piglet'], out_file)
	return get_list()
	
def handle(handler):
	page = BOOTSTRAP_HEADER_HTML + '<h1>List of Whiskies</h1>\n'
	mylist = safe_get_list()
	for item in mylist:
		page = page + '<LI>' + item + '</LI>\n'
	# show pretty button
	page = page + FORM_HTML
	return page
	
def handle_post(handler):
	print 'POST:', handler.command, handler.path
	return handle(handler)
	
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the HTTP GET requests
	def do_common(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()

	def do_GET(self):
		self.do_common()
		self.wfile.write( handle(self) )

	def do_POST(self):
		self.do_common()
		self.wfile.write( handle_post(self) )

if __name__=='__main__':
	HTTPServer(('', PORT_NUMBER), myHandler).serve_forever()



