import string
def getFreqDict(corpus, filterchars=string.punctuation):
    corpus = corpus.lower()
    for c in filterchars:
        corpus = corpus.replace(c,"")
    words = corpus.split()
    words = filter(None,words)
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq.update({word: 1})
    return freq
