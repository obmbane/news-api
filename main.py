import requests as rq
import smtplib, ssl, os

api_key = '99c9d45eaef445e08fe288cced78c6b5'
url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-11-09&sortBy=publishedAt&apiKey=99c9d45eaef445e08fe288cced78c6b5'

request = rq.get(url)
content = request.json()

def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    '''
    username = os.getenv('MY_EMAIL')
    password = os.getenv('EMAIL_PASSWORD')
    receiver = os.getenv('MY_EMAIL')
    '''
    username = 'obmbanetraining@gmail.com'
    password = 'jrsg cigg dafz csci'
    receiver = 'obmbanetraining@gmail.com'

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)
message = 'Latest News: '
for article in content['articles']:

    if article['title'] is not None:
        title = article['title']
        description = article['description']
        message += 2*'\n' + title + '\n' + description + '\n'

message = message.encode('utf-8')
print(message)
#email_content = message
send_email(message)



