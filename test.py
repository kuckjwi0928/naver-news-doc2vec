from naverapi import NaverNewsApi
from crawler import Crawler
from doc2vec import Doc2VecAnalysis
from gensim.models.doc2vec import Doc2Vec

std_in = input('뉴스 검색어를 입력하세요\n')

news_api = NaverNewsApi()

crawler = Crawler(news_api.get_news(std_in))
model = Doc2Vec(Doc2VecAnalysis(crawler.crawling()),
                vector_size=200, window=15, min_count=2, epochs=100, workers=2, hs=0, alpha=0.025)

print(model.wv.most_similar(std_in, topn=10))
