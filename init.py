import obmplib
from tableMaker import Pashmak

class simulation:

    def __init__(self):
        self.tick = 0
        self.lasttick = 0
        self.ableworktime = 0
        self.bakerworktime = 0
        self.ableworking = -1
        self.bakerworking = -1
        self.queue = []
        self.pashmak = None
        self.history = []
        self.works = []
        self.ableworkingnow = None
        self.bakerworkingnow = None
        
    def initpashmak(self, a, b):
        self.pashmak = Pashmak(a, b)
        
    def nexttick(self):
        while (True):
            if (self.ableworking > 0):
                self.ableworking -= 1
                if (self.ableworking == 0):
                    self.ableworking = -1
                    if (self.ableworkingnow):
                        self.ableworkingnow.endtime = self.tick
                        self.works.append(self.ableworkingnow)
                    
            if (self.bakerworking > 0):
                self.bakerworking -= 1
                if (self.bakerworking == 0):
                    self.bakerworking = -1
                    if (self.bakerworkingnow):
                        self.bakerworkingnow.endtime = self.tick
                        self.works.append(self.bakerworkingnow)
            if (self.tick < self.lasttick):
                self.queue.extend(self.pashmak.queue(self.tick))
            
            if (len(self.queue) > 0 and self.ableworking == -1):
                self.ableworking = self.ableworktime
                self.ableworkingnow = self.queue.pop(0)
                self.ableworkingnow.starttime = self.tick
            
            if (len(self.queue) > 0 and self.bakerworking == -1):
                self.bakerworking = self.bakerworktime
                self.bakerworkingnow = self.queue.pop(0)
                self.bakerworkingnow.starttime = self.tick
            
            self.history.append((len(self.queue), self.ableworking, self.bakerworking))
            self.tick += 1

            if (self.tick > self.lasttick and len(self.queue) == 0 and self.ableworking == -1 and self.bakerworking == -1):
                break

sim = simulation()
sim.lasttick = 10000
sim.ableworktime = 5
sim.bakerworktime = 10

sim.initpashmak(0,10)
sim.nexttick()

s = ""

for i in sim.works:
    s += ("Came:" + str(i.queuetime) + ", Started:" + str(i.starttime) + ", Finished:" + str(i.endtime) + ", Time:" + str(i.endtime - i.queuetime))
    s += "\n"

s2 = ""

for i in sim.history:
    kk = i[0]
    if (i[1] != -1):
        kk += 1
    if (i[2] != -1):
        kk += 1
    s2 += str(kk) + "\n"

f = open("s1.txt", 'w')
f.write(s)
f.close()

f = open("s2.txt", 'w')
f.write(s2)
f.close()
