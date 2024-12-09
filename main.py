import requests as rq
import smtplib, ssl, os

api_key = '99c9d45eaef445e08fe288cced78c6b5'
url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-11-09&sortBy=publishedAt&apiKey=99c9d45eaef445e08fe288cced78c6b5'

request = rq.get(url)
content = request.json()

def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = os.getenv('MY_EMAIL')
    password = os.getenv('EMAIL_PASSWORD')
    receiver = os.getenv('MY_EMAIL')

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)


for article in content['articles']:

    print(article['title'])
    print(article['description'])



