from time import sleep
from urllib.request import urlopen
from email_main import Mail

url = input("Webpage to keep track of: ")
mins = int(input("Ping website after every this many seconds: "))
print("When the website gets changed,")
email_to = input("Email to: ")
with_subject = input("Subject line of email: ")
email_body = input("Email body: ")

def emailMe():
    m = Mail()
    m.create_msg(f"{email_to}", f"{with_subject}", f"{email_body}")
    m.send_msg()

def get_html(url):
    html = urlopen(url).read().decode()
    return html

webpage = get_html(url)

while True:

    # Get HTML
    webpage_cmp = get_html(url)

    # If unequal, email
    if (webpage_cmp != webpage):
        emailMe()
        webpage = webpage_cmp
    
    # Sleep for 30 minutes
    sleep(60*mins)