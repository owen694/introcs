idk = (raw_input("please enter some plaintext string:"))
idk = idk.upper()

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def findboi(char, word):
''' assumes char is a character string and text is a string
finds the first index position of char the word
'''
    if char in word:
     for x in range(0,len(word)+1):
      if len[x] == char:
        return x
    else:
      return -1

def testFind():
    '''checks if find works.'''
    pos = 0
    for ch in LETTERS:
        index = find(c,LETTERS)
        print 'ch =', ch , 'index = ', index, 'works? ', pos == index
        pos += 1

def encryptOne(char,shift=3):
    ''' assumes that char is an upercase single char
    shifts the input by 3 on the alphabet'''
        pl = find(char,LETTERS)
        return LETTERS[(pl + 3) % 26]

def testEncryptOne():
    ''' checks if encryptOne works'''
    correct = LETTERS[3:] + LETTERS[:-3]
    for i in range(0,len(LETTERS)):
        cipherCh = encryptOne(LETTERS[i])
        ch = LETTERS[i]
        correctAns = correct[i]
        print 'ch', ch, 'encrypts to', cipherCh, 'correct? ', correctAns == cipherCh

def ecryptWord (word,shift=3):
    ''' assumes that word is an upercase string
    shifts each char in the word over 3 on the alphabet'''
    ans = ''
    for i in word:
        ans += ecryptOne(c)
    return ans

def decryptWord(cipher,shift=-3):
    ''' assumes that word is an uppercase string
    shifts each char in the word back 3 letters in the alphabet'''
    return encryptWord(cipher,shift)

def testEncryption(shift=3):
    '''Verifies the encryptWord() and decryptWord()'''
    words = ["ADRIS", "JAVA", "BEE", "STUYPULSE"]
    #["DGULV", 'MDYD', 'EHH', 'VWXBSXOVH']
    for i in range(0,len(words)):
        plaintext = words[i]
        ciphertext = encryptWord(plaintext, shift)
        decrypttext = decryptWord(ciphertext, -shift)
        print 'plaintext: ', plaintext , 'ciphertext', ciphertext,
        print 'decrypt text=', decrypttext, 'correct? ', plaintext == decrypttext
