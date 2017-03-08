#is an Apache2 Licensed HTTP library, written in Python
#Once you get the data from a server, you can parse it using python a library called BeautifulSoup is often used
from bs4 import BeautifulSoup
import requests
 
# get html data
r = requests.get('https://www.youtube.com/')
html_doc = r.content 

# create a beautifulsoup object
soup = BeautifulSoup(html_doc,"lxml")

 
# get title text
print (soup.title.text)
 
