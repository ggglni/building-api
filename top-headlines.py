import requests

key = 'b03ec8fdc9d14775abcf7ba6b13c7730'

def get_news(country, api_key=key):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={key}'
    r = requests.get(url)
    content = r.json()

    articles = content['articles']
    
    results = []
    
    for article in articles:
        results.append(f"TITLE\n{article['title']}\nDESCRIPTION\n{article['description']}")
        
    return results

print(get_news(country='fr'))
    