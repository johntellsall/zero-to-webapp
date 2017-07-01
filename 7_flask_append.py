"""
7_flask_append.py: Hello World in Flask, with template
adapted from Learn Python the Hard Way, ex 50"
"""

XXXX DOESN'T WORK


# XX for Cloud9
import sys; sys.path.append('./myenv/lib/python3.4/site-packages')

import web
from wtforms import Form, BooleanField, StringField, PasswordField, validators

class NameForm(Form):
	name = StringField('Cat name?') # , validators=[Required()])
	# submit = SubmitField('Submit')

urls = (
	'/', 'index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class index:
	def GET(self):
		greeting = "Hello World"
		return render.index(greeting = greeting)

if __name__ == "__main__":
	app.run()