#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wsgiref.handlers

import webapp2

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
    self.response.out.write('<form action="/submit" method = "post"><input type=text name=word1><br><input type=text name=word2><br><input type=submit value=Submit></form>')


class Word_shuffle(webapp2.RequestHandler):
  def post(self):
    self.response.out.write('<html><body><font size="5" color="skyblue">You wrote:</font><pre>')
    str1 = self.request.get('word1')
    str2 = self.request.get('word2')

  
    self.response.out.write('<font size="5">%s\n'%str1)
    self.response.out.write('%s\n</font>'%str2)
    self.response.out.write('<font size="7" color="pink">Shuffled:</font>')
    
    if len(str1)>len(str2):
      num = len(str2)
    else:
      num = len(str1)
      
    i = 0
    shuffle = []
    
    while i < num: 
      shuffle.append(str1[i])
      shuffle.append(str2[i])
      i += 1
      
    if len(str1)>len(str2):
      shuffle.append(str1[i:])
    else:
      shuffle.append(str2[i:])

    for word in shuffle:
      self.response.out.write('<font size="5" color="forestgreen">%s</font>'%word)
      
    self.response.out.write('</pre></body></html>')
    

app = webapp2.WSGIApplication(
  [('/', MainPage),('/submit',Word_shuffle),],
  debug=True)
