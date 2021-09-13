from nltk import ngrams


class NgramsToken:
    def __init__(self):
        self.n = 2

    def ngram_token(self, word):
        ngrams_t = ngrams(word, self.n)
        ngram_list = []
        for ngram in ngrams_t:
            ngram_list.append(ngram)
        return ngram_list

    def compare_ngram(self, s1, s2):
        count1 = self.ngram_token(s1)
        count2 = self.ngram_token(s2)
        counter1 = self.countElements(count1)
        counter2 = self.countElements(count2)
        similar = 0
        ratio = 0
        if count1 is not None:
            for token in count1:
                for compar in count2:
                    if token == compar:
                        similar += 1
            ratio = similar / (counter2 + counter1)
        return ratio

    def countElements(self, count):
        return len(count)

    def similarityRatio(self, s1, s2):
        ratio1= self.compare_ngram(s1, s2)
        self.n = 3
        ratio2 = self.compare_ngram(s1, s2)
        return (0.5 * ratio1) + (0.5 * ratio2)

if __name__ == '__main__':
    NgramsToken = NgramsToken()
    NgramsToken.ngram_token('fast')
    sim1 = NgramsToken.compare_ngram('heart', 'heat')
    print(sim1)
    NgramsToken.n = 3
    sim2 = NgramsToken.compare_ngram('heart', 'heat')
    print(sim2)
    print(0.5 * sim1 + 0.5* sim2)
    NgramsToken.n = 2
    similar = NgramsToken.similarityRatio('heart', 'heat')
    print(similar)
