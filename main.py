import requests as rq
import smtplib, ssl, os

api_key = '99c9d45eaef445e08fe288cced78c6b5'
topic = 'tesla'
language = 'en'
url = f'https://newsapi.org/v2/everything?q={topic}&from=2024-11-09&sortBy=publishedAt&apiKey={api_key}&language={language}'

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
message = "Subject: Daily News"\
    + '\n'
count = 1
for article in content['articles'][:20]:

    if article['title'] is not None:
        title = article['title']
        description = article['description']
        article_url = article['url']
        message += '\n' + str(count) + ')'+' ' + title + '\n'+ description + '\n' + article_url + 2*'\n'
        count += 1

message = message.encode('utf-8')
print(message)
#email_content = message
send_email(message)



