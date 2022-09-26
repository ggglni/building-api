import requests

url = 'https://api.languagetoolplus.com/v2/check'

data = { #we pass the parameters through a dictionary
    'text': 'Hello, how are you?',
    'language': 'en-US'
}
response = requests.post(url, data=data)

print(response.text)