from cltk import NLP
from gensim.models import Word2Vec
import gensim 
#from cltk.languages.example_texts import get_example_text

latin_nlp = NLP("lat")
latin_nlp.pipeline.processes.pop(-1)
sentences = []



stopword = ['ab', 'ac', 'ad', 'adhic', 'aliqui', 'aliquis', 'an', 'ante', 'apud', 
          'at', 'atque', 'aut', 'autem', 'cum', 'cur', 'de', 'deinde', 'dum', 
          'ego', 'enim', 'ergo', 'es', 'est', 'et', 'etiam', 'etsi', 'ex', 'fio',
            'haud', 'hic', 'iam', 'idem', 'igitur', 'ille', 'in', 'infra', 'inter',
              'interim', 'ipse', 'is', 'ita', 'magis', 'modo', 'mox', 'nam', 'ne', 'nec', 
              'necque', 'neque', 'nisi', 'non', 'nos', 'o', 'ob', 'per', 'possum', 'post', 
              'qui', 'quia', 'quicumque', 'quidem', 'quilibet', 'quis', 
              'quisnam', 'quisquam', 'quisque', 'quisquis', 'quo', 'quoniam', 
              'sed', 'si', 'sic', 'sive', 'sub', 'sui', 'sum', 'super', 'suus', 
              'tam', 'tamen', 'trans', 'tu', 'tum', 'ubi', 'uel', 'uero',
            'unus', 'ut', '.', ',', ';', '?', '\'', '!']
stopwords = set(stopword)

# f = open("aeneid_tokens.txt", "w")
for i in range(9,13):
    if i == 3 or i == 6 or i == 8:
        continue
    textname = open(f'testing/latin/text/vergil/aen{i}.txt', "r")
    latin_text = textname.read()
    print(i)
    latin_doc = latin_nlp.analyze(latin_text)
    # sentences = []  # This is what you want
    for sentence in latin_doc.sentences:
        lemmatized_words = []
        for word in sentence.words:
            if word.lemma not in stopwords:
                lemmatized_words.append(word.lemma)
        sentences.append(lemmatized_words)


model = gensim.models.Word2Vec(sentences, window=6, min_count=2, workers=5)

print(len(sentences))



keyword1 = 'amor'
print(keyword1)
words1 = model.wv.most_similar(positive=keyword1, topn=20)
print(words1)

keyword2 = 'bellum'
print(keyword2)
words2 = model.wv.most_similar(positive=keyword2, topn=20)
print(words2)

keyword3 = 'deus'
print(keyword3)
words3 = model.wv.most_similar(positive=keyword3, topn=20)
print(words3)