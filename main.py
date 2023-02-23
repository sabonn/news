import news

search = 'israel'#searching for news
url = news.text_url(search)
html = news.get_html('h3',url)
urls, titles = news.getting_titles_urls(html)
for i in range(len(titles)):
    print(f'title: {titles[i]}\nurl: {urls[i]}')