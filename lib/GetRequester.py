import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content
       

    def load_json(self):
        response_text = self.get_response_body() # gives the raw json string
        return json.loads(response_text) #returns that string into real python object