#!/usr/bin/env python3
from xml.dom import minidom
import urllib.request
import urllib
def main(argv):
  baseurl='http://54.92.123.84/search?ackey=869388c0968ae503614699f99e09d960f9ad3e12&q=Body:'
  maxnum=0
  for v in argv:
      with urllib.request.urlopen(baseurl+urllib.parse.quote(v)) as req:
          doc = minidom.parseString(req.read())
          num = int(doc.getElementsByTagName('result')[0].getAttribute('numFound'))
          if maxnum<=num:
              maxnum=num
              maxv=v

  print('{{name: {0}, count: {1}}}'.format(maxv,maxnum))

