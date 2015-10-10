import obmplib, turtle
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
        workername = ''
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
                self.ableworkingnow.servname = 'able'
            
            if (len(self.queue) > 0 and self.bakerworking == -1):
                self.bakerworking = self.bakerworktime
                self.bakerworkingnow = self.queue.pop(0)
                self.bakerworkingnow.starttime = self.tick
                self.bakerworkingnow.servname = 'baker'
            
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


able = {}
baker = {}

hpot = {}
hpot2 = {}

s = ""
s3 = ""

for i in sim.works:
    b = i.endtime - i.queuetime
    s += (str(b))
    s += "\n"
    s3 += (str(i.starttime - i.queuetime))
    s3 += "\n"
    if (hpot.get(i.starttime - i.queuetime)):
        hpot[i.starttime - i.queuetime] += 1
    else:
        hpot[i.starttime - i.queuetime] = 1

    if (hpot2.get(i.endtime - i.queuetime)):
        hpot2[i.endtime - i.queuetime] += 1
    else:
        hpot2[i.endtime - i.queuetime] = 1

    
    if i.servname == 'able':
        b -= sim.ableworktime
        if b in able:
            able[b] += 1
        else:
            able[b] = 1
    else:
        b -= sim.bakerworktime
        if b in baker:
            baker[b] += 1
        else:
            baker[b] = 1

f = open("s1.txt", 'w')
f.write(s)
f.close()

f = open("s3.txt", 'w')
f.write(s3)
f.close()

s4 = ""
for i in hpot:
    s4 += str(i) + '\t' + str(hpot[i]) + '\n'

f = open("s4.txt", 'w')
f.write(s4)
f.close()

s7 = ""
for i in hpot2:
    s7 += str(i) + '\t' + str(hpot2[i]) + '\n'

f = open("s7.txt", 'w')
f.write(s7)
f.close()


s2 = ""

for i in sim.history:
    kk = i[0]
    if (i[1] != -1):
        kk += 1
    if (i[2] != -1):
        kk += 1
    s2 += str(kk) + "\n"



f = open("s2.txt", 'w')
f.write(s2)
f.close()

# print(able)
# print(baker)

a = open('s5.txt', 'w')
for i in able:
    a.write("%d\t%d\n" % (i, able[i]))
a.close()

a = open('s6.txt', 'w')
for i in baker:
    a.write("%d\t%d\n" % (i, baker[i]))
a.close()

# wn = turtle.Screen()
# wn.delay(0)
# wn.screensize(200, 200)
# wn.setworldcoordinates(0, 0, 80, 80)
# wn.exitonclick()


def makeUnderLine(u):
    p = t.pos()
    while t.pos()[0] > -320:
        t.bk(5)
        t.pu()
        t.bk(5)
        t.pd()

    t.write(str(u), align='left', font=('Times New Roman', 10))
    t.pu()
    t.goto(*p)
    t.pd()

t = turtle.Turtle()
turtle.delay(0)
t.speed(0)
t.hideturtle()
t.pensize(4)
t.pu()
t.goto(-300, -200)
t.pd()
t.fd(600)
t.pu()
t.goto(-300, -200)
t.pd()
t.goto(-300, +200)
t.pu()
t.pensize(2)
t.pencolor('red')
t.goto(-280, +180)
t.write("Able", align='left', font=('Times New Roman',16))
t.goto(-300, -200)
t.pd()

l1 = sorted(able.keys(), key=lambda x: x)
l11 = sorted(able.keys(), key=lambda x: able[x])

l2 = sorted(baker.keys(), key=lambda x: x)
l22 = sorted(baker.keys(), key=lambda x: baker[x])

d1 = 400 / max(able[l11[-1]], baker[l22[-1]])
d2 = 600 / max(l1[-1], l2[-1])

for i in l1:
    t.goto(i * d2 - 280, able[i] * d1 - 200)
    # makeUnderLine(able[i])
    t.write(str((able[i], i)), align='left', font=('Times New Roman', 10))

t.pu()
t.pencolor('blue')
t.goto(-240, +180)
t.write("Baker", align='left', font=('Times New Roman', 16))
t.goto(-300, -200)
t.pd()

for i in l2:
    t.goto(i * d2 - 280, baker[i] * d1 - 200)
    #print(i, baker[i])
    # makeUnderLine(baker[i])
    t.write(str((baker[i], i)),align='left',font=('Times New Roman', 10))


turtle.done()
