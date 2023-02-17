import requests
from bs4 import BeautifulSoup

#start of scrap functios
def get_html(search, url):#getting the html from the url that was passed
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    titles = soup.find_all(search)
    return titles


def text_url(search):#taking a search topic and turning it into a news.google url to search for articles
    search = search.replace(' ', '+')
    url = f'https://news.google.com/search?q={search}'
    return url


def getting_titles_urls(html):#getting the titles of the articles and links for them
    urls = set()
    texts = []
    for i in html:
        link = i.find('a')
        if link is not None:
            url = f'https://news.google.com{link["href"][1:]}'
            if url not in urls:
                urls.add(url)
        text = link.text.strip() if link is not None else ''
        if text and text not in texts:
            texts.append(text)
    return (list(urls), texts)
#end of scrap functions