import json
import requests
from lxml import html

def scrap():
	data = requests.get("https://www.dailymotion.com/embed/video/k68WMVFZuolZKWkZD3I")
	
	tree = html.fromstring(data.text)
	scripts = tree.xpath('//script/text()')
	for script in scripts:
		lines = script.split('\n ')
		for line in lines:
			l = line.strip()
			configPrefix = "var config = "
			if l.startswith(configPrefix):
				l = l[len(configPrefix):]
				url = getAuthUrl(l.strip())
				getStreamURL(url,data.cookies)
			
def getStreamURL(authurl,cookies):
	data = requests.get(authurl,cookies=cookies)
	print data.text
	
	
def getAuthUrl(js):
	js = js.replace("\n","")
	js = js.replace(r'\"','')
	obj = json.loads(js[:len(js)-1]) # trim last ;
	return obj["metadata"]["qualities"]["auto"][0]["url"]
	

if __name__=="__main__":
	scrap()