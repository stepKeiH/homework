# coding: UTF-8
import cgi
from google.appengine.api import users
import webapp2
import urllib
import urllib2
import random

MAIN_PAGE_HTML = """\
<html>
  <body>
    <form action="/convert" method="get">
      <div><textarea name="message" rows="3" cols="60"></textarea></div>
      <div><input type="submit" value="Convert to"></div>
    </form>
    <form action="/show" method="get">
      <div><textarea name="message" rows="3" cols="60"></textarea></div>
      <div><input type="submit" value="Show"></div>
    </form>
    <form action="/getword" method="get">
      <select name="pos">
        <option value="verb">動詞</option>
        <option value="noun">名詞</option>
        <option value="adjective">形容詞</option>
        <option value="adverb">副詞</option>
        <option value="exclamation">感嘆詞</option>
        <option value="preposition">前置詞</option>
        <option value="conjunction">接続詞</option>
        <option value="interjection">間投詞</option>
    　</select>
    <p><input type="submit" value="送信"></p>
    </form>
    <form action="/madlib" method="get">
      <BUTTON type="submit">**madlib**</BUTTON><BR><BR>
    </form>
  </body>
</html>
"""


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class Convert(webapp2.RequestHandler):

    def get(self):
        # self.response.write('<html><body>You wrote:<pre>')
        #self.response.write(cgi.escape(self.request.get('message')))
        self.response.headers['Content-Type'] = 'text/plain'
        messe = self.request.get('message')
        rev_mes = messe[::-1]
        self.response.write(rev_mes)

class Show(webapp2.RequestHandler):

    def get(self):
        # gc = gspread.login('account@gmail.com','password')
        url_list = urllib2.urlopen('http://step15-krispop.appspot.com/peers').read().split()

        self.response.headers['Content-Type'] = 'text/plain'
        messe = self.request.get('message')
        data = urllib.urlencode({'message': messe})
        for url in url_list:
            try:
              result = urllib2.urlopen(url + '/convert?' + data).read()
              self.response.write(url + ' => ' + result +'\n\n')

            except urllib2.URLError, e:
              handleError(e)

class Getword(webapp2.RequestHandler):

    def get(self):
        messe = self.request.get('pos')
        pos_dict = {'verb': 'eat', 'noun':'apple', 'adjective': 'healthy',
         'adverb': 'always', 'exclamation': '!!!!', 'preposition': 'for', 'conjunction': 'nevertheless',
          'interjection': 'alas'}
        if messe in pos_dict:
            self.response.write(pos_dict[messe])
        else:
            self.response.write('google')

class Madlib(webapp2.RequestHandler):

    def get(self):
        # url_list = ['http://step15-krispop.appspot.com', 'http://kei-step2015.appspot.com']
        url_list = urllib2.urlopen('http://step15-krispop.appspot.com/peers').read().split()
        count = 0
        ans_list = ["noun", "verb", "adverb", "exclamation"]
        num = len(url_list) - 1
        while count < 4:
            i = random.randint(0, num)
            url = url_list[i]
            try:
                result = urllib2.urlopen(url + '/getword?pos=' + ans_list[count]).read()
                ans_list[count] = result
                count += 1
            except urllib2.HTTPError:
                continue

        self.response.write(' '.join(ans_list))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/convert', Convert),
    ('/show', Show),
    ('/getword', Getword),
    ('/madlib', Madlib)
], debug=True)
