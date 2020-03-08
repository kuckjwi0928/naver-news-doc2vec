from konlpy.tag import Mecab
from gensim.models.doc2vec import TaggedDocument


class Doc2VecAnalysis(object):
    def __init__(self, contents):
        self.mecab = Mecab()
        self.contents = contents

    def __iter__(self):
        for i, content in enumerate(self.contents):
            yield TaggedDocument(self.mecab.morphs(content), ['SENT_%s' % i])
