import requests
import json

GOOGLE_URL_SHORTEN_API = 'AIzaSyCeZMN-uyaLrbEACHreeLJLFzGBi2LvoJY'

def google_url_shorten(url):
   req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=' + GOOGLE_URL_SHORTEN_API
   payload = {'longUrl': url}
   headers = {'content-type': 'application/json'}
   r = requests.post(req_url, data=json.dumps(payload), headers=headers)
   resp = json.loads(r.text)
   return resp['id']