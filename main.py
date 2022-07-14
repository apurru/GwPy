import requests
from bs4 import BeautifulSoup

def google(user_text):
	
	text = user_text.replace(' ',"+")
	URL = f"https://www.google.com/search?q={text}&aqs=chrome.1.69i57j0i7i3019.10583j0j7&sourceid=chrome&ie=UTF-8"
	headers = {'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
	page = requests.get(URL, headers=headers)
	soup = BeautifulSoup(page.content, "html.parser")
	result = soup.find('span', class_='hgKElc').get_text()
	
	return print(result) 


while True:
	h = input("What is your question?: ")
	google(h)
