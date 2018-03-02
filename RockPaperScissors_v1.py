'''Angel Li, Period 7'''

#takes player input
player1 = (raw_input(" enter your choice <rock,paper,scissors>"))
player2 = (raw_input(" enter your choice <rock,paper,scissors>"))

#function that assumes a is player 1 and b is player 2 and determines which won the game rock,paper, scissors
def rps(a,b):
    if a == b:
        print "it's a tie"
    elif ((a == "paper") and (b == "rock")) or  ((a == "rock") and (b == "scissors")) or  ((a == "scissors") and (b =="paper")):
        print "player 1 won!"
    else:
        print "player 2 won!"

'''conditional, first checks if the inputs are actually rock/paper/scissors'''
if ((player1 != "rock") and (player1 != "scissors") and (player1 != "paper")) or ((player2 != "rock") and (player2 != "scissors") and (player2 != "paper")) :
    print "please enter a valid input"
else:
    rps(player1, player2)
