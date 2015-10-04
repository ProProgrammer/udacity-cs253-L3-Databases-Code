import os
import webapp2
import jinja2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
	autoescape=True)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.write(*a, **kw)

	def render_str(self,template,**params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainPage(Handler):
	def render_front(self, title="", artwork="", error=""):
		"""
		This function is created to avoid code duplication as we are going to render form using "self.render" quite a few times
		"""
		self.render("front.html", title=title, artwork=artwork, error=error)

	def get(self):
		# self.render("front.html")
		self.render_front()

	def post(self):
		title = self.request.get('title')
		art = self.request.get('art')

		if title and art:
			self.write('Thanks!')
		else:
			error = "We need both, a title and an artwork!"
			self.render_front(title=title, artwork=art, error=error)

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)