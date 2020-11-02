from gensim.models import KeyedVectors
import numpy as np
class word2vec:
    model = KeyedVectors.load_word2vec_format("path to w2v model/sbw_vectors.bin",binary=True)

    def __init__(self):
        self.data = []

    def similarity(self, word, wordcompare):
        if word in self.model.wv.vocab and wordcompare in self.model.wv.vocab:
            dis1 = self.model.wv.similarity(word, wordcompare)
            return dis1
        else:
            return 0

    #def wordvector(self, word):
     #   if word in self.model.wv.vocab:
      #      wordvector = self.model.wv[word]
       # else:
       #     wordvector = [0] * 300
       # return wordvector
    
    def wordvector(self,words):
        wordvectorsuma=[]
        ngram=words.split()
        for word in ngram:
            if word in self.model.wv.vocab:
                if(len(wordvectorsuma)==0):
                    wordvectorsuma=np.array(self.model.wv[word])
                else:
                    wordvectorsuma = wordvectorsuma+np.array(self.model.wv[word])   
            else:
                if(len(wordvectorsuma)==0):
                    wordvectorsuma = [0] * 300
                else:
                    wordvectorsuma = wordvectorsuma+np.array(0)
        wordvectorsuma = np.array(wordvectorsuma)/len(ngram)
        return wordvectorsuma

