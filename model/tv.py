from google.appengine.ext import ndb

class Tv(ndb.Model):
    name = ndb.StringProperty()
    link = ndb.StringProperty()