import unittest
import urllib.request
import urllib.parse
import http.cookiejar
import json
import sys

class TestHttpbin(unittest.TestCase):
    def test_httpbin_get(self):
        url = "http://httpbin.org/get"
        data = {}
        data['params1'] = 'urllib.1'
        data['params2'] = 'urllib.2'
        data['params3'] = 'urllib.3'
        url_values = urllib.parse.urlencode(data)
        full_url = url + '?' + url_values

        try:
            cj = http.cookiejar.CookieJar()
            opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
            response = opener.open(full_url)
            # response.headers.get('Set-Cookie') # get cookies
        except urllib.error.URLError as e:
            print(e.reason)

        string = response.read().decode('utf-8')
        json_obj = json.loads(string)

        self.assertEqual( data['params3'] , json_obj["args"]["params3"])
