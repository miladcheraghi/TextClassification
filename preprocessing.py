from __future__ import unicode_literals
from hazm import *
import pprint
import re

normalizer = Normalizer()

f = open("TempSample.txt","r")
new = True
sample = ""
while new:
    new = f.readline()
    sample = sample + new

global stopWord
stopWord = []
f = open("StopWord.txt","r")
for line in f:
    stopWord.append(line.replace("\n",""))


def postToWord( postString ):
    # Keep only Persian characters.
    persianOnly = re.sub("[^آ-ی]",  # The pattern to search for
                         " ",       # The pattern to replace it with
                         postString)      # The text to search
    # remove half distance and ...
    persianOnly = normalizer.normalize(persianOnly)
    # tokenize post
    persianWords = word_tokenize(persianOnly)
    # remove stop words
    meaningfulWords = [str(w) for w in persianWords if not w in stopWord]
    return (" ".join( meaningfulWords ))
