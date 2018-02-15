
import random
n = int(raw_input("enter a #: "))
#n = 9

rollDie = lambda x: random.randint(0,x)

print rollDie(n)
