''' Angel Li, Period 7 '''
import random

def rps(a,b):
    if a == b:
        print "it's a tie"
    elif ((a == "paper") and (b == "rock")) or  ((a == "rock") and (b == "scissors")) or  ((a == "scissors") and (b =="paper")):
        print "player won!"
    else:
        print "computer won!"

p1 = (raw_input(" enter your choice <rock,paper,scissors>"))
# checks if player input is valid
if ((p1 != "rock") and (p1 != "scissors") and (p1 != "paper")):
    print "please enter a valid input"
p2 = random.randint(1,3)
if p2 == 1:
    p2 = "rock"
elif p2 == 2:
    p2 = "paper"
elif p2 == 3:
    p2 = "scissors"
print p2

rps(p1,p2)
