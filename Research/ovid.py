from cltk import NLP
from gensim.models import Word2Vec
import gensim 
#from cltk.languages.example_texts import get_example_text

latin_nlp = NLP("lat")
latin_nlp.pipeline.processes.pop(-1)
sentences = []



keyword = 'vis'
stopword = ['ab', 'absum','ac', 'ad', 'adsum', 'adhic', 'aliqui', 'aliquis', 'alius', 'an', 'ante', 'apud', 
          'ago', 'at', 'atque', 'aut', 'autem', 'cum', 'cur', 'de', 'deinde', 'dum', 'do', 'dico', 'ecce',
          'ego', 'enim', 'ergo', 'et', 'etiam', 'etsi', 'ex', 'facio', 'fio', 'hinc',
            'haud', 'hic', 'iam', 'idem', 'igitur', 'ille', 'in', 'intro', 'infra', 'inter','noster', 'nequiquam',
              'interim', 'ipse', 'is', 'ita', 'magis', 'meus', 'modo', 'multus', 
              'medius', 'mitto', 'mox', 'nam', 'ne', 'nec', 'nullus', 
              'necque', 'neque', 'nisi', 'non', 'nos', 'o', 'ob', 'per', 'pro', 'possum', 'post',
              'postquam',  'peto', 'omnis', 'habeo', 'video', 'iterum', 'propterea',  'paro', 'pars',
              'qui', 'quia', 'quicumque', 'quidem', 'quilibet', 'quis', 'res', 'saepe', 'nimius', 'quaero',
              'quisnam', 'quisquam', 'quisque', 'quisquis', 'quo', 'quoque', 'quod', 'quam',
              'quoniam', 'sequor', 'sedeo', 'tantus', 'talis', 'reddo', 'sine', 'sive',
              'sed', 'si', 'sic', 'siue', 'sub', 'sui', 'sum', 'super', 'suus', 'usus', 'ullus', 'tuus',
              'tam', 'tamen', 'trans', 'tu', 'tum', 'totus','utor', 'ubi', 'uel', 'uero', 'utque' , 'nunc',
            'unus', 'ut', '.', ',', ';', '?', '\'', '\'', '(', ')', "!"]
stopwords = set(stopword)

file1 = open("MyFile.txt", "w")
# # f = open("aeneid_tokens.txt", "w")
for i in range(1,4):

    textname = open(f'testing/latin/text/ovid/ovid.amor{i}.txt', "r")
    latin_text = textname.read()
    print(i)
    latin_doc = latin_nlp.analyze(latin_text)
    # sentences = []  # This is what you want
    for sentence in latin_doc.sentences:
        lemmatized_words = []
        for word in sentence.words:
            if word.lemma not in stopwords:
                lemmatized_words.append(word.lemma)
                file1.write(word.lemma + " ")
        if keyword in lemmatized_words:
            sentences.append(lemmatized_words)

for i in range(1,4):
    if i == 2:
        continue

    textname = open(f'testing/latin/text/ovid/ovid.artis{i}.txt', "r")
    latin_text = textname.read()
    print(i)
    latin_doc = latin_nlp.analyze(latin_text)
    # sentences = []  # This is what you want
    for sentence in latin_doc.sentences:
        lemmatized_words = []
        for word in sentence.words:
            if word.lemma not in stopwords:
                lemmatized_words.append(word.lemma)
                file1.write(word.lemma + " ")
        if keyword in lemmatized_words:
            sentences.append(lemmatized_words)

for i in range(1,7):
    if i == 3:
        continue

    textname = open(f'testing/latin/text/ovid/ovid.fasti{i}.txt', "r")
    latin_text = textname.read()
    print(i)
    latin_doc = latin_nlp.analyze(latin_text)
    # sentences = []  # This is what you want
    for sentence in latin_doc.sentences:
        lemmatized_words = []
        for word in sentence.words:
            if word.lemma not in stopwords:
                lemmatized_words.append(word.lemma)
                file1.write(word.lemma + " ")
        if keyword in lemmatized_words:
            sentences.append(lemmatized_words)

for i in range(1,22):
    if i == 1:
        continue

    textname = open(f'testing/latin/text/ovid/ovid.her{i}.txt', "r")
    latin_text = textname.read()
    print(i)
    latin_doc = latin_nlp.analyze(latin_text)
    # sentences = []  # This is what you want
    for sentence in latin_doc.sentences:
        lemmatized_words = []
        for word in sentence.words:
            if word.lemma not in stopwords:
                lemmatized_words.append(word.lemma)
                file1.write(word.lemma + " ")
        if keyword in lemmatized_words:
            sentences.append(lemmatized_words)

file1.close()

model = gensim.models.Word2Vec(sentences, window=10, min_count=2, workers=5)

print(len(sentences))


print(keyword)
words1 = model.wv.most_similar(positive=keyword, topn=30)
print(words1)

# keyword2 = 'bellum'
# print(keyword2)
# words2 = model.wv.most_similar(positive=keyword2, topn=20)
# print(words2)

# keyword3 = 'deus'
# print(keyword3)
# words3 = model.wv.most_similar(positive=keyword3, topn=20)
# print(words3)

# # keyword4 = 'dea'
# # print(keyword4)
# # words4 = model.wv.most_similar(positive=keyword4, topn=20)
# # print(words4)

# keyword5 = 'lux'
# print(keyword5)
# words5 = model.wv.most_similar(positive=keyword5, topn=20)
# print(words5)

# keyword6 = 'manus'
# print(keyword6)
# words6 = model.wv.most_similar(positive=keyword6, topn=20)
# print(words6)