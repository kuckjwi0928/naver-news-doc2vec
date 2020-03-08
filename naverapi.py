from requests import get
from json import loads
from config import NAVER_CLIENT_ID, NAVER_CLIENT_SECRET


class NaverNewsApi:
    NAVER_NEWS_API_URI = 'https://openapi.naver.com/v1/search/news.json'

    def get_news(self, query):
        content = get(self.NAVER_NEWS_API_URI, {
            'query': query,
            'display': 100,
        }, headers={
            'X-Naver-Client-Id': NAVER_CLIENT_ID,
            'X-Naver-Client-Secret': NAVER_CLIENT_SECRET,
        }).content
        return loads(content)
