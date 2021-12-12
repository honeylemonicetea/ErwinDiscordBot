import numpy as np
import spacy
from spacy import displacy

# nlp = spacy.load('en_core_web_trf')
#
# with open('text_test1.txt') as file:
#     text = file.read()
#
# doc = nlp(text)
#
# # for num, item in enumerate(doc.sents):
# #     for token in item:
# #         print(item.pos_)
# # Sentences
# # sents = list(doc.sents)
# # first_sentence = sents[0]
# # for i in first_sentence:
# #     print(f"{i} \t| lemma: {i.lemma_}, \t| pos: {i.pos_}")
#
# # LABELS
# entities = list(doc.ents)
# # for entity in entities:
# #     print(f"{entity} \t| Label: {entity.label_} ")
# displacy.render(doc, style="ent")
WORD = 'magic'

nlp = spacy.load("en_core_web_md")
with open('movies.txt') as text:
    data = text.read()
doc = nlp(data)
# for num, sentence in enumerate(doc.sents):
#     print(f"{num}|\t{sentence}")

sents = list(doc.sents)

sentence = nlp('it was the most horrible terrifying horror')
print(sentence)
print(sentence.sentiment)