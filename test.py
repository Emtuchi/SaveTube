import urllib.parse
import os

def username_from_url(url):
        parsed = urllib.parse.urlparse(url)
        print(parsed)

username_from_url("")