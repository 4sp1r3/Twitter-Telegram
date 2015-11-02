import json
import requests

# To get admin user account:
resp = requests.post(
	'https://api.telegram.org/bot{}/getUpdates'.format(
		os.environ.get('BOT_ACCESS_TOKEN')))
response = json.loads(resp.text)
result = response['result']
if len(result) is 0:
    print "Please"
else:
    your_id = result[0]['message']['from']['id']
    print(your_id)
