import json
import requests
from lxml import html

class dailymotion:
	def scrap(self,url):
		data = requests.get(url,verify=True)
		
		tree = html.fromstring(data.text)
		scripts = tree.xpath('//script/text()')
		for script in scripts:
			lines = script.split('\n ')
			for line in lines:
				l = line.strip()
				configPrefix = "var config = "
				if l.startswith(configPrefix):
					l = l[len(configPrefix):]
					url = self.getAuthUrl(l.strip())
					return self.getStreamURL(url,data.cookies)
				
	def getStreamURL(self,authurl,cookies):
		data = requests.get(authurl,cookies=cookies)
		return data.url
		
	def getAuthUrl(self,js):
		js = js.replace("\n","")
		js = js.replace(r'\"','')
		obj = json.loads(js[:len(js)-1]) # trim last ;
		return obj["metadata"]["qualities"]["auto"][0]["url"]
	