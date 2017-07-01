'''
webapp v4: show list of items from function
'''

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

DATA_PATH = 'mylist.txt'

def get_list():
	out = []
	with open(DATA_PATH) as data_file:
		for line in data_file:
			out.append(out)
	return out

def handle(handler):
	page = BOOTSTRAP_HEADER_HTML + '<h1>List of Whiskies</h1>\n'
	mylist = get_list()
	for item in mylist:
		page = page + '<LI>' + item + '</LI>\n'
	# show pretty button
	page = page + '<button type="button" class="btn btn-primary">Primary</button>'
	return page
	

class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the HTTP GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write( handle(self) )

if __name__=='__main__':
	HTTPServer(('', PORT_NUMBER), myHandler).serve_forever()



