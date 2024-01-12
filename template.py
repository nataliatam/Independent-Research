# For most users, this is the only import required
import string
from cltk import NLP
from gensim.models import Word2Vec
import gensim 

latin_nlp = NLP(language="lat")
latin_nlp.pipeline.processes.pop(-1)


keyword = 'example' # this is the desired keyword
stopword = ['ab', 'absum','ac', 'ad', 'adsum', 'adhic', 'aliqui', 'aliquis', 'alius', 'an', 'ante', 'apud', 
          'ago', 'at', 'atque', 'aut', 'autem', 'cum', 'cur', 'de', 'deinde', 'dum', 'do', 'dico', 'ecce',
          'ego', 'enim', 'ergo', 'es', 'est', 'et', 'etiam', 'etsi', 'ex', 'facio', 'fio', 'hinc',
            'haud', 'hic', 'iam', 'idem', 'igitur', 'ille', 'in', 'intro', 'infra', 'inter','noster', 'nequiquam',
              'interim', 'ipse', 'is', 'ita', 'magis', 'meus', 'modo', 'multus', 
              'medius', 'mitto', 'mox', 'nam', 'ne', 'nec', 'nullus', 
              'necque', 'neque', 'nisi', 'non', 'nos', 'o', 'ob', 'per', 'pro', 'possum', 'post',
              'postquam',  'peto', 'omnis', 'iterum', 'propterea', 'pars', 'qui', 
              'quia', 'quicumque', 'quidem', 'quilibet', 'quis', 'res', 'saepe', 'nimius', 'quaero',
              'quisnam', 'quisquam', 'quisque', 'quisquis', 'quo',  'quod', 'quam',
              'quoniam', 'tantus', 'talis', 'sine', 'sed', 'si', 'sic', 'siue', 'sub', 'sui', 'sum', 'super', 
              'suus', 'usus', 'ullus', 'unus', 'ut', 'tuus', 'tam', 'tamen', 'trans', 'tu', 'tum', 'totus','utor', 'ubi', 'uel', 'uero', 'utque' , 'nunc']
stopwords = set(stopword)

tokens = []

print(len(tokens)) # The number of sentences found with the token
model = gensim.models.Word2Vec(tokens, window=10, min_count=2, workers=10)

print(keyword)
words1 = model.wv.most_similar(positive=keyword, topn=20)
print(words1)