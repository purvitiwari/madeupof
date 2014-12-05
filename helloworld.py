import webapp2
import sys
import urllib2
import os
import jinja2
import re
import logging
import json
import urlparse

sys.path.insert(0, 'libs')
# from bs4 import BeautifulSoup

#setting up jinja2 to pick files from templates dir
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

#Shorthand functions to make life easier
class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainHandler(BaseHandler):
    def get(self):
        self.render("index.html")


class Scrape(BaseHandler):
    def get(self):
        url = 'http://builtwith.com/' + self.request.get('url')
        content = urllib2.urlopen(url).read()
        stidx = content.find('div class="span8"') - 1
        enidx = content.find('div class="span4"') - 1
        
        self.response.headers['Content-Type'] = 'application/json'
        urls = json.dumps([{'url': content[stidx:enidx]}])
        obj = {
            "urls" : urls
            }
        self.response.out.write("{\"urls\" : " + urls + " }")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/scrape/.*', Scrape)
], debug=True)
