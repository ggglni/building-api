import requests

key = 'b03ec8fdc9d14775abcf7ba6b13c7730'

# r = requests.get(f'https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-9-22&to=2022-9-21&sortBy=popularity&language=en&apiKey={key}')

# content = r.json()

# #print(content['articles'][3]['title'])

# articles = content['articles']

# for article in articles:
#     print('TITLE\n', article['title'], '\nDESCRIPTION\n', article['description'])
    
def get_news(topic, from_date, to_date, language='en', api_key=key):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={key}'
    
    r = requests.get(url)
    
    content = r.json()

    articles = content['articles']
    
    results = []
    
    for article in articles:
        results.append(f"TITLE\n{article['title']}\nDESCRIPTION\n{article['description']}")
        
    return results[0]

print(get_news('Meloni','2022-09-01','2022-09-10'))
    