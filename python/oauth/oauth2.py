#!/usr/bin/env python
# -*- coding: utf-8 -*-

# <http://www.18th-technote.com/Python%E3%81%A8OAuth%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6Tumblr%E3%81%AB%E6%8A%95%E7%A8%BF%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95>
# sudo easy_install oauth2
 
import oauth2
import urlparse
 
REQUEST_TOKEN_URL = 'http://www.tumblr.com/oauth/request_token'
 
CONSUMER_KEY = '[Consumer Key]'
CONSUMER_SECRET = '[Consumer Secret]'
 
def main():
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    client = oauth2.Client(consumer)
    resp, content = client.request(REQUEST_TOKEN_URL, 'GET')
    request_token = dict(urlparse.parse_qsl(content))
    print 'Request Token: %s' % request_token['oauth_token']
    print 'Request Token Secret: %s' % request_token['oauth_token_secret']
 
if __name__ == '__main__':
    main()
