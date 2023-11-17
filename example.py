from cltk import NLP
vitruvius = "pluribus disciplinis et variis eruditionibus ornata, quae ab ceteris artibus perficiuntur. Opera ea nascitur et fabrica et ratiocinatione"
cltk_nlp = NLP(language="lat")
cltk_nlp.pipeline.processes.pop(-1)
'''cltk_doc = cltk_nlp.analyze(vitruvius)
print(cltk_doc.tokens[0:])
print(cltk_doc.lemmata[0:])'''
print(cltk_nlp.pipeline.processes)

textname = open("testing/latin/text/lat_text_latin_library/vergil/aen1.txt", "r")
text = textname.read()
textname.close()
text = cltk_nlp.analyze(text)
#tokens = text.tokens[0:]
lemma_tokens = text.sentences_tokens.lemmata[0:20]
print(lemma_tokens)



