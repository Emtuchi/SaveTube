import re

def is_valid_url(url):
    # Regular expression for a simple URL validation
    url_pattern = re.compile(r'https?://\S+')
    return bool(url_pattern.match(url))

def is_valid_username(username):
    # Regular expression for username validation (allowing only letters, numbers, and underscores)
    username_pattern = re.compile(r'^\w+$')
    return bool(username_pattern.match(username))