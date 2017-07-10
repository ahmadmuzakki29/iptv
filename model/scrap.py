from google.appengine.ext import ndb

class Scrap(ndb.Model):
	type = ndb.StringProperty() # type of scrap ex: dailymotion
	url = ndb.StringProperty()
	streamURL = ndb.StringProperty()
	last_update = ndb.DateTimeProperty()