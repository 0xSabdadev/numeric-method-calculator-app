import json

def read_json(path):
    with open(path) as json_file:
        return json.load(json_file)

def remove_dash(url):
    url = url.replace("-", " ", 1)
    url = url.replace("-", "/", 1)
    return url
