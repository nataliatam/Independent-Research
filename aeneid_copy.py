# For most users, this is the only import required
import string
from cltk import NLP
from gensim.models import Word2Vec
import gensim 

cltk_nlp = NLP(language="lat")
cltk_nlp.pipeline.processes.pop(-1)



stopwords = ['ab', 'ac', 'ad', 'adhic', 'aliqui', 'aliquis', 'an', 'ante', 'apud', 
          'at', 'atque', 'aut', 'autem', 'cum', 'cur', 'de', 'deinde', 'dum', 
          'ego', 'enim', 'ergo', 'es', 'est', 'et', 'etiam', 'etsi', 'ex', 'fio',
            'haud', 'hic', 'iam', 'idem', 'igitur', 'ille', 'in', 'infra', 'inter',
              'interim', 'ipse', 'is', 'ita', 'magis', 'modo', 'mox', 'nam', 'ne', 'nec', 
              'necque', 'neque', 'nisi', 'non', 'nos', 'o', 'ob', 'per', 'possum', 'post', 
              'qui', 'quia', 'quicumque', 'quidem', 'quilibet', 'quis', 
              'quisnam', 'quisquam', 'quisque', 'quisquis', 'quo', 'quoniam', 
              'sed', 'si', 'sic', 'sive', 'sub', 'sui', 'sum', 'super', 'suus', 
              'tam', 'tamen', 'trans', 'tu', 'tum', 'ubi', 'uel', 'uero', 'unus', 'ut']
to_be_removed = set(stopwords)
f = open("aeneid_tokens.txt", "w")
tokens = []
for i in range(1,13):
    textname = open(f'testing/latin/text/edit_text/vergil/aen{i}.txt', "r")
    text = textname.read()
    text = text.translate(str.maketrans('', '', string.punctuation))
    textname.close()

    text = cltk_nlp.analyze(text)
    temp = text.lemmata[0:]

    lemma_tokens = [i for i in temp if i not in to_be_removed] 

    for items in lemma_tokens:
        f.write("%s " % items)
    f.write("\n")

    tokens.append(lemma_tokens)



for i in range(1,11):
    textname = open(f'testing/latin/text/edit_text/vergil/ec{i}.txt', "r")
    text = textname.read()
    text = text.translate(str.maketrans('', '', string.punctuation))
    textname.close()

    text = cltk_nlp.analyze(text)
    temp = text.lemmata[0:]

    lemma_tokens = [i for i in temp if i not in to_be_removed] 

    for items in lemma_tokens:
        f.write("%s " % items)
    f.write("\n")
    
    tokens.append(lemma_tokens)
f.close()

print(tokens)


# for i in range(1,5):
#     textname = open(f"testing/latin/text/lat_text_latin_library/vergil/geo{i}.txt", "r")
#     text = textname.read()
#     text = text.translate(str.maketrans('', '', string.punctuation))
#     textname.close()

#     text = cltk_nlp.analyze(text)
#     lemma_tokens = text.lemmata[0:]
#     tokens.append(lemma_tokens)

# model = gensim.models.Word2Vec(tokens, window=6, min_count=4, workers=5)
# model.train(tokens,total_examples=len(tokens),epochs=1)

# print(len(tokens))

# keyword1 = 'amor'
# print(keyword1)
# words1 = model.wv.most_similar(positive=keyword1, topn=20)
# print(words1)

# keyword2 = 'bellum'
# print(keyword2)
# words2 = model.wv.most_similar(positive=keyword2, topn=20)
# print(words2)

# keyword3 = 'deus'
# print(keyword3)
# words3 = model.wv.most_similar(positive=keyword3, topn=20)
# print(words3)

# keyword4 = 'lumen'
# print(keyword4)
# words4 = model.wv.most_similar(positive=keyword4, topn=20)
# print(words4)

# keyword5 = 'lux'
# print(keyword5)
# words5 = model.wv.most_similar(positive=keyword5, topn=20)
# print(words5)

# keyword6 = 'manus'
# print(keyword6)
# words6 = model.wv.most_similar(positive=keyword6, topn=20)
# print(words6)
