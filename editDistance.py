class EditDistance:
    def __init__(self, i, j):
        self.label_dict = {}
        self.i = i
        self.j = j
        self.m = []
        for a in range(0, i):
            new = []
            for b in range(0, j):
                new.append(0)
            self.m.append(new)

    def editDistance(self, s1, s2):
        for i in range(1, self.i):
            self.m[i][0] = i
        for j in range(1, self.j):
            self.m[0][j] = j
        for i in range(1, len(s1)):
            for j in range(1, len(s2)):
                self.m[i][j] = self.minValue(i, j, s1, s2)
        return self.m[len(s1)-1][len(s1)-1]

    def minValue(self, i, j, s1, s2):
        a = 0
        if s1[i] == s2[j]:
            a = self.m[i - 1][j - 1]
        else:
            a = self.m[i - 1][j - 1] + 1
        b = self.m[i - 1][j] + 1
        c = self.m[i][j - 1] + 1
        return min(a, b, c)


if __name__ == '__main__':
    editDistance = EditDistance(5, 5)
    value = editDistance.editDistance('cast', 'fast')
    print(editDistance.m)
    print(value)
