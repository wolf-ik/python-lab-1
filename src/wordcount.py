import re, collections


class WordCount(object):
    def __init__(self, text):
        self._words = collections.Counter()
        self._average_words_in_sentence = 0
        self._word_excludes = ('', ' ', '-', '\n')

        text = re.sub('[!?]', '.', text)
        text = re.sub('\.\.\.', '.', text)
        text = re.sub('[\n:,;()]', '', text)
        sentences = text.split('.')
        words = [word for sentence in sentences for word in sentence.split(' ') if word not in self._word_excludes]
        self._average_words_in_sentence = float(len(words)) / len(sentences)
        for word in words:
            self._words[word] += 1

    def get_words(self):
        return self._words.most_common(len(self._words))

    def get_average_words(self):
        return self._average_words_in_sentence

    def get_median(self):
        pos = len(self._words) / 2
        t = self._words.most_common(pos)[pos - 1]
        return t[0], t[1]

    def n_gramm(self, k=10, n=4):
        counter = collections.Counter()
        for word in self._words:
            for i in xrange(len(word) - n):
                counter[word[i:i+n]] += 1
        return counter.most_common(k)
