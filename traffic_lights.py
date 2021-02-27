from numpy import random
from heapq import *


#Time latency for chaning the lights from red to green when car is queue and Passage Time.
Tc = 30
Tp = 10


class States_Traffic:
    def wait1(self): # for the car waiting
        return self.cars

    def __init__(self):
        self.green = False
        self.cars = 0

    def greencheck(self):  #for if the light is green return true
        return self.green

    def destroy1(self):  #for empty waiting cars
        self.cars = 0

    def __str__(self):   #for showing the crossroads as status
        return "Green light =" + str(self.green) + ", cars=" + str(self.cars)

    def red1(self): # for turning on the lights
        self.green = False

    def caraddition(self):   # for adding a car in queue by adding +1
        self.cars = self.cars + 1

    def green1(self):  # for turning on the lights
        self.green = True


class States_events:
    def __lt__(self, other):  #for comapring the events with eachother in priority sorted order
        return self.t < other.t

    def __str__(self):  # for displaying events
        return self.name + "(" + str(self.t) + ")"

    def def_time(self):   # for showing def_time at which event process starts
        return self.t


class R2G(States_events):
    def action(self, queue, States_Traffic):
        queue.puts1(G2R(self.t + States_Traffic.wait1() * Tp))
        States_Traffic.green1()
        States_Traffic.destroy1()

    def __init__(self, def_time):
        self.t = def_time
        self.name = "R2G"


class CAR(States_events): #for car functions.

    def action(self, queue, States_Traffic): #for performing actions
        if not States_Traffic.greencheck():
            States_Traffic.caraddition()
            if States_Traffic.wait1() == 1:
                queue.puts1(R2G(self.t + Tc))

    def __init__(self, def_time): # for initiazalioion of car events
        self.t = def_time
        self.name = "CAR"


class QueueStates:

    def check1(self):   # for displaying true if the queue is not empty
        return len(self.q) > 0

    def puts1(self, States_events):  #for creating new events
        heappush(self.q, States_events)

    def __init__(self):
        self.q = []

    def move(self): # for displaying queue for returns and removes for next event
        return heappop(self.q)

    def lastones(self):  # for displaying events for awating
        return len(self.q)


class G2R(States_events):
    def action(self, queue, States_Traffic):
        States_Traffic.red1()

    def __init__(self, def_time):
        self.t = def_time
        self.name = "G2R"



#Main funtion
events = QueueStates()

events.puts1(CAR(10))
events.puts1(CAR(25))
events.puts1(CAR(35))
events.puts1(CAR(60))
events.puts1(CAR(75))

# for showing it randomly uncomment the following
# random.seed(1)
# initalizerandom = 80
# newvalue = 100
# for i in range(1, newvalue):
#    initalizerandom = random.randint(initalizerandom+1, initalizerandom+10)
#    events.puts1( CAR(initalizerandom))


State1 = States_Traffic()
while events.check1(): #dispalying events untill queue is full
    show = events.move()
    print(show)
    show.action(events, State1)