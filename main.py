import webapp2

from tv.all import All
from tv.tv import Tv
from model.tv import Tv as TvModel

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write('Hello, World!')

class Create(webapp2.RequestHandler):
	def get(self):
		tv = TvModel(name="MetroTv",url="http://edge.metrotvnews.com:1935/live-edge/smil:metro.smil/playlist.m3u8")
		tv.put()

app = webapp2.WSGIApplication([
	('/', MainPage),
	('/tv/all',All),
	(r'/tv/(\w+)',Tv),
	('/create',Create),
], debug=True)