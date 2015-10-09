import random


class obj:
    def __init__(self):
        self.starttime = None
        self.endtime = None
        self.queuetime = -1
        self.servname = None

class Pashmak():
    table = [0]
    tableLen = 0

    def __init__(self, start=1, end=8):
        self.start = start
        self.end = end
        self.len = end - start + 1
        self.p = 1.0 / self.len

        self.__makeTable()
        self.table.pop(0)

    def __makeTable(self): 
        for i in range(40):
            self.table.append(self.table[-1] + int(random.random() / self.p))
        self.tableLen += 40

    def queue(self, time):
        data = []

        while self.table[-1] < time:
            self.__makeTable()

        for i in range(self.tableLen):
            if time == self.table[i]:
                ii = obj()
                ii.queuetime = time
                data.append(ii)

        return data

