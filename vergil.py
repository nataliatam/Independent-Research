# For most users, this is the only import required
import string
from cltk import NLP
from gensim.models import Word2Vec
import gensim 

cltk_nlp = NLP(language="lat")
cltk_nlp.pipeline.processes.pop(-1)

tokens = []


for i in range(1,4):
    textname = open(f"testing/latin/text/vergil/aen{i}.txt", "r")
    text = textname.read()
    text = text.translate(str.maketrans('', '', string.punctuation))
    textname.close()
    # print(text)

    text = cltk_nlp.analyze(text)
    lemma_tokens = text.lemmata[0:]
    # print(lemma_tokens)
    tokens.append(lemma_tokens)

for i in range(1,11):
    textname = open(f"testing/latin/text/vergil/ec{i}.txt", "r")
    text = textname.read()
    #text = text.translate(str.maketrans('', '', string.punctuation))
    textname.close()
    # print(text)

    text = cltk_nlp.analyze(text)
    lemma_tokens = text.lemmata[0:]
    # print(lemma_tokens)
    tokens.append(lemma_tokens)

model = gensim.models.Word2Vec(tokens, window=10, min_count=2, workers=10)

print(len(tokens))
#print(tokens[0:75])

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

# keyword4 = 'dea'
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