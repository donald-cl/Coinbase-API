import urllib2
import urllib
import time
import json
import hmac
import hashlib

class BaseCoinbaseAPI(object):

    def __init__(self, access_key, access_signature, access_nonce, version=None):
        self.domain = 'api.coinbase.com'
        self.protocol = 'https://'
        self.version = version if version else 'v1'

        self.access_key = access_key
        self.access_signature = access_signature
        self.access_nonce = access_nonce if access_nonce else int(time.time())

    def _format_request(self, path):
        url = '%s%s/%s/%s' % (
                self.protocol,
                self.domain,
                self.version,
                path)
        return url

    def _get_headers(self):
        headers = {
                'Accept' : 'application/json',
                'Content-Type' : 'application/json',
                'User-Agent' : 'Python',
                'ACCESS_KEY' : self.access_key,
                'ACCESS_SIGNATURE' : self.access_signature,
                'ACCESS_NONCE' : self.access_nonce,
                }
        return headers

    def _format_headers(self, url, body):
        self.access_nonce = int(time.time())
        headers = self._get_headers()
        message = str(self.access_nonce) + url + body
        signature = hmac.new(
                self.access_signature, message, hashlib.sha256).hexdigest()
        headers.update({'ACCESS_SIGNATURE' : signature})
        return headers

    def make_request(self, path, method, body_args=None, query_args=None):
        url = self._format_request(path)
        url += "?" + urllib.urlencode(query_args) if query_args else ''
        body = json.dumps(body_args) if body_args else ''
        headers = self._format_headers(url, body)

        print url
        print "----"
        print headers
        print "----"
        print body

        resp = None
        opener = urllib2.build_opener()
        req = urllib2.Request(url, data=body, headers=headers)

        try:
            resp = opener.open(req)
        except Exception, e:
            print e

        return resp
