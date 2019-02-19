# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.


#For shared gui delegate:
def sprint_3(self, speed):
    print('Got sprint 3 from m2', speed)
    m2_sprint_3.sprint3(self, int(speed))


def bark_m2(self):
    print('Got bark from m2')
    m2_sprint_3.bark(self)

def trick_1_m2(self, speed):
    print('Got trick 1 from m2')
    m2_sprint_3.trick_1(self, int(speed))

def trick_2_m2(self, speed):
    print('Got trick 2 from m2')
    m2_sprint_3.trick_2(self, int(speed))