# [START imports]
import os

import jinja2
import webapp2

import json
import base64
import urllib

from google.appengine.api import urlfetch

# If not using templates, skip this
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]

SHOPIFY_API_KEY = os.environ['SHOPIFY_API_KEY']
SHOPIFY_API_PASSWORD = os.environ['SHOPIFY_API_PASSWORD']
SHOP_URL = os.environ['SHOP_URL']

AUTH_HEADERS = {
    "Authorization": "Basic %s" % base64.b64encode(SHOPIFY_API_KEY+":"+SHOPIFY_API_PASSWORD),
    "Content-Type": "application/json",
}


def shopPOST(endpoint, json_data):
    payload = json.dumps(json_data)

    print 'Payload:'
    print payload

    result = urlfetch.fetch(url=SHOP_URL+endpoint,
        payload=payload,
        method=urlfetch.POST,
        headers=AUTH_HEADERS)
    return result


def shopGET(endpoint, params=None):

    url = SHOP_URL+endpoint
    if params:
        url = url + '?' + urllib.urlencode(params)

    result = urlfetch.fetch(url=url,
                            deadline=60,
                            method=urlfetch.GET,
                            headers=AUTH_HEADERS)
    return result


class Test(webapp2.RequestHandler):

    def get(self):

        query = {
            "limit": 25
        }
        api_result = shopGET("products.json", query)
        status_code = api_result.status_code

        if status_code == 200:
            products = json.loads(api_result.content)["products"]

            self.response.write(str(len(products)) + ' products found: <br /><br />')

            for product in products:
                self.response.write(product['title'] + '<br />')

        else:
            self.abort(status_code)


application = webapp2.WSGIApplication([
    ('/?', Test)
], debug=True)
