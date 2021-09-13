import operator

from editDistance import EditDistance
from nGram import NgramsToken

class SpellCorrect:
    def __init__(self):
        self.maximumWordLength = 4
        self.allVocabulary = {}
        self.allScore = {}
        self.allWords = ['heat', 'bear', 'care', 'mare', 'here', 'hare', 'fail', 'pass', 'good', 'cool', 'fate', 'mate',
                         'gate', 'male', 'tear', 'fear', 'gear', 'flex', 'year', 'wear', 'area', 'deer', 'kite',
                         'hear']

    def spellcheck(self, word):
        gramsToken = NgramsToken()
        editDistance = EditDistance(self.maximumWordLength, self.maximumWordLength)
        for wrd in self.allWords:
            value = editDistance.editDistance(word, wrd)
            self.allVocabulary[wrd] = value
        sorted_d = sorted(self.allVocabulary.items(), key=operator.itemgetter(1))
        top1 = sorted_d[0][0]
        similar1 = gramsToken.similarityRatio(word, top1)
        self.allScore[top1] = similar1
        top2 = sorted_d[1][0]
        similar2 = gramsToken.similarityRatio(word, top2)
        self.allScore[top2] = similar2
        top3 = sorted_d[2][0]
        similar3 = gramsToken.similarityRatio(word, top3)
        self.allScore[top3] = similar3
        top4 = sorted_d[3][0]
        similar4 = gramsToken.similarityRatio(word, top4)
        self.allScore[top4] = similar4
        top5 = sorted_d[4][0]
        similar5 = gramsToken.similarityRatio(word, top5)
        self.allScore[top5] = similar5
        print(self.allScore)
        sorted_d = sorted(self.allScore.items(), key=operator.itemgetter(1), reverse=True)
        print(sorted_d[0])
        return sorted_d[0][0]


if __name__ == '__main__':
    SpellCorrect = SpellCorrect()
    correctWord = SpellCorrect.spellcheck('fite')
    print(correctWord)
