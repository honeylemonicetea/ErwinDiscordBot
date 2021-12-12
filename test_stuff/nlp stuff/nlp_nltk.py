import nltk
from nltk.tokenize import word_tokenize
# import nltk.book as book_txts
import string

with open('movies.txt') as file:
    file1 = file.read()
#
file1 = word_tokenize(file1.translate(dict.fromkeys(string.punctuation)))

text1 = nltk.FreqDist(file1)
#
print(text1.most_common())
