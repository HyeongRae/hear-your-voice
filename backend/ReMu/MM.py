import requests
import json

def send(text, path):
    requests.post('MMlink', 
        data=json.dumps({"attachments": [{
            "color": "#FF8000",
            "text": str(text),
            "author_name": "django",
            "author_icon": "http://www.mattermost.org/wp-content/uploads/2016/04/icon_WS.png",
            "title": path,
        }]}),
        headers={'Content-Type': 'application/json'}
    )
