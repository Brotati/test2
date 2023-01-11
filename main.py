import requests

url = ' http://elastic.bmapsbd.com/test/parse/search'
obj = {'q': 'mohakhali'}

x = requests.post(url, data = obj)

print(x.json())