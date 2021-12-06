import requests # http requests
from bs4 import BeautifulSoup # web scraping
# sending email
import smtplib
# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# system date and time manipulation
import datetime
# get environment variables
import os
# load environment variables
from dotenv import load_dotenv
load_dotenv()

# get current system time and store in 'now' variable
now = datetime.datetime.now()

# email content placeholder
content = ""

# extracting Hacker News stories


def extract_news(url):
    print("Extracting Hacker News Stories...")
    cnt = ""
    cnt +=("<b>HN Top Stories:</b>\n" + "<br>" + "-" * 50 + "<br>")
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    
    for i, tag in enumerate(soup.find_all("td", attrs={"class": "title", "valign": ""})):
        cnt += ((str(i + 1) + " :: " + tag.text + "\n" + "<br>") if tag.text != "More" else "")
        
        #print(tag.prettify) #find_all("span", attrs={"class": "sitestr"}))
    return (cnt)

cnt = extract_news("https://news.ycombinator.com/")
content += cnt
content += ("<br>------<br>")
content += ("<br><br>End of Message")

# send the email

print("Composing Email...")

# update your email details

SERVER = os.environ["SERVER"]
PORT = os.environ["PORT"]
FROM = os.environ["FROM"]
TO = os.environ["TO"]
PASS = os.environ["PASS"]

msg = MIMEMultipart()

msg["Subject"] = "Top News Stories HN [Automated Email]" + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)

msg["From"] = FROM
msg["To"] = TO

msg.attach(MIMEText(content, "html"))

print("Initializing Server...")

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print("Email Sent...")

server.quit()