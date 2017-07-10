import webapp2

from model.tv import Tv


class All(webapp2.RequestHandler):
	def get(self):
		self.response.write("#EXTM3U\n")
		
		tvs = Tv.query()
		for tv in tvs:
			self.response.write("#EXTINF:-1,"+tv.name+"\n")
			self.response.write(tv.url+ "\n")
