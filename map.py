import random


class Map:
    def __init__(self):
        self.size = 0
        self.map = [[0 for i in range(2)] for j in range(2)]
        self.score = 0

    def copyMap(self):
        newMap = [[0 for i in range(self.size)] for j in range(self.size)]
        for a,i in enumerate(self.map):
            for b,j in enumerate(i):
                newMap[a][b] = self.map[a][b]
        return newMap

    def same(self, oriMap):
        if oriMap == self.map:
            return False
        return True

    def setMap(self, size):
        self.size = size
        self.map = [[0 for i in range(self.size)] for j in range(self.size)]
        self.score = 0


    def add(self, num):
        numNum = random.choice([2, 2, 2, 2, 2, 2, 2, 4])
        emptyCnt = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.map[i][j] == 0:
                    emptyCnt += 1
                    if emptyCnt == num:
                        self.map[i][j] = numNum
                        return

    def getCnt(self):
        cnt = 0
        for row in self.map:
            for box in row:
                if box != 0:
                    cnt += 1
        return cnt

    def cal(self, row):
        if len(row) == 0:
            for i in range(self.size):
                row.append(0)
            return row
        cnt = 0
        for i in row:
            if i == row[cnt - 1] and cnt != 0:
                self.score += (row[cnt - 1] * 2)
                row[cnt - 1] *= 2
                row[cnt] = 0
            cnt += 1
        for i in row:
            if i == 0:
                row.remove(0)
        box = self.size - len(row)
        if box == 0:
            return row
        for i in range(box):
            row.append(0)
        return row

    def operate(self, direc):
        if direc == 'w':
            for i in range(self.size):
                row = []
                for j in range(self.size):
                    if self.map[j][i] != 0:
                        row.append(self.map[j][i])
                row = self.cal(row)
                for t in range(self.size):
                    self.map[t][i] = row[t]
        elif direc == 'a':
            for i in range(self.size):
                row = []
                for j in range(self.size):
                    if self.map[i][j] != 0:
                        row.append(self.map[i][j])
                row = self.cal(row)
                for t in range(self.size):
                    self.map[i][t] = row[t]
        elif direc == 's':
            for i in range(self.size):
                row = []
                for j in range(self.size):
                    if self.map[self.size - j - 1][i] != 0:
                        row.append(self.map[self.size - j - 1][i])
                row = self.cal(row)
                for t in range(self.size):
                    self.map[self.size - t - 1][i] = row[t]
        elif direc == 'd':
            for i in range(self.size):
                row = []
                for j in range(self.size):
                    if self.map[i][self.size - j - 1] != 0:
                        row.append(self.map[i][self.size - j - 1])
                row = self.cal(row)
                for t in range(self.size):
                    self.map[i][self.size - t - 1] = row[t]
