import requests
from bs4 import BeautifulSoup
import smtplib

URL='https://www.amazon.in/Fujifilm-Instax-LiPlay-Hybrid-Instant/dp/B07STF9PQJ/ref=sr_1_12_sspa?crid=2WWQ1OOLHOEC1&dchild=1&keywords=polaroid+camera&qid=1605157685&sprefix=pola%2Caps%2C351&sr=8-12-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVU85S01YWTBLN1VUJmVuY3J5cHRlZElkPUEwODE4OTI3M0g2STIwWkQ1UkdGRCZlbmNyeXB0ZWRBZElkPUEwMzE1Nzk0MzVYUVBBSEZRRjg0TiZ3aWRnZXROYW1lPXNwX210ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}

def check_price():
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    title=soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_dealprice").get_text()
    converted_price=price[2:8]
    converted_price=converted_price.replace(',','')
    converted_price=float(converted_price)

    if(converted_price <  10,000):
        send_mail()
    print(converted_price)
    print(title.strip())

    if(converted_price < 10,000):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('dikshanasa01@gmail.com','nhftmeeiowfldjkf')
    
    subject ='Price fell down!'
    body = 'Check the amazon link https://www.amazon.in/Fujifilm-Instax-LiPlay-Hybrid-Instant/dp/B07STF9PQJ/ref=sr_1_12_sspa?crid=2WWQ1OOLHOEC1&dchild=1&keywords=polaroid+camera&qid=1605157685&sprefix=pola%2Caps%2C351&sr=8-12-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVU85S01YWTBLN1VUJmVuY3J5cHRlZElkPUEwODE4OTI3M0g2STIwWkQ1UkdGRCZlbmNyeXB0ZWRBZElkPUEwMzE1Nzk0MzVYUVBBSEZRRjg0TiZ3aWRnZXROYW1lPXNwX210ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'dikshanasa01@gmail.com',
        'dikshanasa01@gmail.com',
        msg 
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()


check_price()



