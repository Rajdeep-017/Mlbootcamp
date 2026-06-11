'''
multithreading for I/O bound tasks
The scenario is web scrapping.
web scrapping often involves making numerous network requests to fetch web
pages.This task are I o bound because they spend a lot of time waiting for responses from the server.
https://www.langchain.com/
https://www.langchain.com/#observability
'''
import threading
import requests
from bs4 import BeautifulSoup

url=[
'https://www.langchain.com/',
'https://www.langchain.com/#observability'
]
def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'fetch {len(soup.text)}')

threads=[]
for u in url:
    thread=threading.Thread(target=fetch_content,args=(u,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()

print("fetchedd @!!!!")

