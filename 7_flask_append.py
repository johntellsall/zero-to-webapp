"""
6_flask.py: Hello World in Flask, with template
from Learn Python the Hard Way, ex 50"
"""
import web
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
	name = StringField('Cat name?', validators=[Required()])
	submit = SubmitField('Submit')

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