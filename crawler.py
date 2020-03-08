from bs4 import BeautifulSoup
from selenium import webdriver
from requests import get


class Crawler:
    def __init__(self, news_result):
        self.news_result = news_result
        self.chrome_options = webdriver.ChromeOptions()

    def crawling(self):
        contents = []
        self.chrome_options.add_argument('headless')
        self.chrome_options.add_argument('disable-gpu')
        for item in self.news_result['items']:
            try:
                link = item['originallink']
                if not link:
                    continue
                elif not link.startswith('http'):
                    link = 'http:' + link
                print(f'''{item['title']}, {link}''')
                soup = BeautifulSoup(get(link, timeout=3000).content, 'lxml')
                body = soup.body
                style_tags = body.find_all('style')
                script_tags = body.find_all('script')
                for tag in style_tags + script_tags:
                    if tag:
                        tag.extract()

                for text in body.text.split('\n'):
                    t = text.strip()
                    if t and len(t) >= 100:
                        contents.append(t)
            except Exception as e:
                print(e)
        return contents
