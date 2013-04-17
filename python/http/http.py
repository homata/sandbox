#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://coreblog.org/ats/python-http-module-request
# sudo easy_install requests


'''
import urllib2
request = urllib2.Request("http://homata.com:18080/rest/admin/account/admin/@all?mid=th&xoauth_requestor_id=60004")
request.add_header('User-Agent','My Sweet Web Robot')
opener = urllib2.build_opener()
body = opener.open(request).read()
print body
'''

# https://pypi.python.org/pypi/requests
import requests
r = requests.get("http://homata.com:18080/rest/admin/account/admin/@all?mid=th&xoauth_requestor_id=60004")
print r.content
