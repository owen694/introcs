idk = (raw_input("please enter some plaintext string:"))
idk.upper()

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def findboi(char, word):
''' this does the thing that was asked of me'''
    if char in word:
     for x in range(0,len(word)+1):
      if len[x] == char:
        return x
    else:
      return -1


def encryptOne(char):
    return LETTERS[findboi(char,letters) + 2]
