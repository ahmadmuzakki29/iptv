import math
import webapp2
from datetime import datetime
from google.appengine.ext import ndb
from model.scrap import Scrap

class Tv(webapp2.RequestHandler):
	def get(self,tvkey):
		key = ndb.Key(Scrap, tvkey)
		scr = key.get()
		if not self.is_still_valid(scr.last_update):
			scr = self.doScrap(scr)
			scr.last_update = datetime.now()
			scr.put()
		self.response.write(scr.streamURL)

	def doScrap(self,scr):
		type = scr.type
		mod = __import__('scrapper.'+type, fromlist=[type])
		klass = getattr(mod, type)()
		scr.streamURL = klass.scrap(scr.url)
		return scr
	
	def post(self,tvkey):
		scr = Scrap(id=tvkey,type="dailymotion",url="http://www.dailymotion.com/embed/video/x4nwi47")
		scr.put()
		self.response.write('ok')
	
	def is_still_valid(self,last_update):
		if last_update==None:
			return False
		
		after = datetime.now()
		d = (after - last_update)
		minutes,seconds = divmod(d.days * 86400 + d.seconds, 60)
		if minutes>60:
			return False
		return True