from cltk import NLP
from gensim.models import Word2Vec
import gensim 
#from cltk.languages.example_texts import get_example_text

latin_nlp = NLP("lat")
latin_nlp.pipeline.processes.pop(-1)
sentences = []


keyword = 'potestas'
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
              'quoniam', 'sequor', 'sedeo', 'tantus', 'talis', 'reddo', 'sine', 'sive',
              'sed', 'si', 'sic', 'siue', 'sub', 'sui', 'sum', 'super', 'suus', 'usus', 'ullus', 'tuus',
              'tam', 'tamen', 'trans', 'tu', 'tum', 'totus','utor', 'ubi', 'uel', 'uero', 'utque' , 'nunc',
            'unus', 'ut', '.', ',', ';', '?', '\'', '\'', '(', ')', "!"]
stopwords = set(stopword)

for i in range(1,9):

    textname = open(f'testing/latin/text/caesar/gall{i}.txt', "r")
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
            sentences.append(lemmatized_words)
    textname.close()


for i in range(1,4):
    textname = open(f'testing/latin/text/caesar/bc{i}.txt', "r")
    latin_text = textname.read()
    print(i)
    latin_doc = latin_nlp.analyze(latin_text)
    for sentence in latin_doc.sentences:
        lemmatized_words = []
        for word in sentence.words:
            if word.lemma not in stopwords:
                lemmatized_words.append(word.lemma)
        if keyword in lemmatized_words:
            sentences.append(lemmatized_words)
    textname.close()


model = gensim.models.Word2Vec(sentences, window=10, min_count=2, workers=5)

print(len(sentences))



print(keyword)
words1 = model.wv.most_similar(positive=keyword, topn=30)
print(words1)

