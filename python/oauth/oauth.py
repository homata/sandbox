#!/usr/bin/env python
# -*- coding: utf-8 -*-

# <http://taichino.com/programming/1057>
 
import urllib
from oauth import oauth
 
# ユーザ登録時にもらえる情報
consumer_key = 'your consumer key (public key)'
secret_key   = 'your private key'
 
# リクエストしたいURLとパラメータ
url   = 'http://query.yahooapis.com/v1/yql'
params = {
  'q'      : 'show tables',
  'format' : 'json'
}
 
# 1. Consumerオブジェクト作成
consumer = oauth.OAuthConsumer(consumer_key, secret_key)
# 2. HTTPリクエスト組み立て
request  = oauth.OAuthRequest.from_consumer_and_token(consumer, None, http_url=url, parameters=params)
# 3. リクエストに署名して発行
request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(), consumer, None)
stream = urllib.urlopen(request.to_url())
print stream.read()
