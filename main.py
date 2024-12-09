import requests as rq

api_key = '99c9d45eaef445e08fe288cced78c6b5'
url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-11-09&sortBy=publishedAt&apiKey=99c9d45eaef445e08fe288cced78c6b5'

request = rq.get(url)
content = request.json()

for article in content['articles']:

    print(article['title'])
    print(article['description'])

    

