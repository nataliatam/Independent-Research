# For most users, this is the only import required
import string
from cltk import NLP
from gensim.models import Word2Vec
import gensim 

latin_nlp = NLP(language="lat")
latin_nlp.pipeline.processes.pop(-1)


keyword = 'pietas'
stopword = ['ab', 'absum','ac', 'ad', 'adsum', 'adhic', 'aliqui', 'aliquis', 'alius', 'an', 'ante', 'apud', 
          'ago', 'at', 'atque', 'aut', 'autem', 'cum', 'cur', 'de', 'deinde', 'dum', 'do', 'dico', 'ecce',
          'ego', 'enim', 'ergo', 'es', 'est', 'et', 'etiam', 'etsi', 'ex', 'facio', 'fio', 'hinc',
            'haud', 'hic', 'iam', 'idem', 'igitur', 'ille', 'in', 'intro', 'infra', 'inter','noster', 'nequiquam',
              'interim', 'ipse', 'is', 'ita', 'magis', 'meus', 'modo', 'multus', 
              'medius', 'mitto', 'mox', 'nam', 'ne', 'nec', 'nullus', 
              'necque', 'neque', 'nisi', 'non', 'nos', 'o', 'ob', 'per', 'pro', 'possum', 'post',
              'postquam',  'peto', 'omnis', 'habeo', 'video', 'iterum', 'propterea',  'paro', 'pars',
              'qui', 'quia', 'quicumque', 'quidem', 'quilibet', 'quis', 'res', 'saepe', 'nimius', 'quaero',
              'quisnam', 'quisquam', 'quisque', 'quisquis', 'quo',  'quod', 'quam',
              'quoniam', 'sequor', 'sedeo', 'tantus', 'talis', 'reddo', 'sine', 
              'sed', 'si', 'sic', 'siue', 'sub', 'sui', 'sum', 'super', 'suus', 'usus', 'ullus', 'tuus',
              'tam', 'tamen', 'trans', 'tu', 'tum', 'totus','utor', 'ubi', 'uel', 'uero', 'utque' , 'nunc',
            'unus', 'ut', '.', ',', ';', '?', '\'', '\'', '(', ')', "!"]
stopwords = set(stopword)

tokens = []

for i in range(1, 13):
    if i == 1 or i == 3 or i == 6 or i == 8:
      continue
    print(i)
    textname = open(f'testing/latin/text/vergil/aen{i}.txt', "r")
    latin_text = textname.read()
    latin_doc = latin_nlp.analyze(latin_text)
    sentences = []  # This is what you want
    for sentence in latin_doc.sentences:
        lemmatized_words = []
        for word in sentence.words:
            if word.lemma not in stopwords:
                lemmatized_words.append(word.lemma)
                # file1.write(word.lemma + " ")
        if keyword in lemmatized_words:
            tokens.append(lemmatized_words)
    textname.close()

for i in range(1,11):
    if i == 6 or i == 8:
        continue
    textname = open(f'testing/latin/text/vergil/ec{i}.txt', "r")
    latin_text = textname.read()
    print(i)
    latin_doc = latin_nlp.analyze(latin_text)
    # sentences = []  # This is what you want
    for sentence in latin_doc.sentences:
        lemmatized_words = []
        for word in sentence.words:
            if word.lemma not in stopwords:
                lemmatized_words.append(word.lemma)
        if keyword in lemmatized_words:
            tokens.append(lemmatized_words)


print(len(tokens))
model = gensim.models.Word2Vec(tokens, window=10, min_count=2, workers=10)

print(len(tokens))


print(keyword)
words1 = model.wv.most_similar(positive=keyword, topn=30)
print(words1)

