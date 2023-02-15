import requests
from bs4 import BeautifulSoup


def get_html(search):
    url = text_url(search)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    titles = soup.find_all('h3')
    return titles


def text_url(search):
    search = search.replace(' ', '+')
    url = f'https://news.google.com/search?q={search}'
    return url


def title_url(titles):
    urls = []
    for title in titles:
        link = title.find('a')
        if link:
            url = link['href']
            url = f'https://news.google.com{url[1:]}'
            if url in urls:
                continue
            urls.append(url)
    return urls

def get_title(urls):
    link = urls[0]
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    titles = soup.find_all('h1')
    return titles[0]

def execute(inp):
    titles = get_html(inp)
    urls = title_url(titles)
