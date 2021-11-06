import re
from collections import Counter
from mpi4py import MPI

import nltk
from razdel import sentenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def tokenize_by_sent(text):
    return [_.text for _ in (sentenize(text))]


def validation(word):
    match = re.match("^[А-Яа-яё]+$", word)
    return bool(match)


def divide_chunks(l, n):
    return [l[i::n] for i in range(n)]


nltk.download('punkt')
nltk.download('stopwords')
ru_stop_words = set(stopwords.words('russian'))

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

with open('data/war_and_peace.txt') as fin:
    input_text = ' '.join(fin.readlines())

if rank == 0:
    sentences = tokenize_by_sent(input_text)
    segments = divide_chunks(sentences, size)

else:
    segments = None

segment = comm.scatter(segments, root=0)

tokens = word_tokenize(' '.join(segment), language='russian')
tokens = [word.lower() for word in tokens if validation(word)]
filtered_words = [word.lower() for word in tokens if word not in ru_stop_words]
word_counts = Counter(filtered_words)

word_counts = comm.gather(word_counts, root=0)

if rank == 0:
    top_words = sum(word_counts, Counter()).most_common(10)
    print("Top word")
    for i, word in enumerate(top_words):
        print("{0} - {1}:{2}".format(i, word[0], word[1]))
