def pigLatin (pig):
    if (pig == "?") or (pig==","):
        return pig
    else:
        pigLat = ''
        vowels = 'AEIOU'
        n = 0
        pig = pig.upper()
        if pig[0] in vowels:
            smth = pig + 'WAY'
            return smth
        else:
            for c in pig:
                if c in vowels:
                    pigLat = pig[n:]
                    break
                n += 1
            smth = pigLat + pig[0:n] + 'AY'
            return smth
    

def find(sub,s, start = 0):
    gap = len(sub)
    if sub not in s:
        return -1
    x = 0
    for i in range(start, len(s)):
        if sub == s[i: i + gap]:
            return i
   


def punc(char, sen):
    if char in sen:
        a = find(char,sen)
        sen = sen[:a] + (' ' + sen[a:])
    return sen


def spac(sen):
    sen = punc("?",sen)
    sen = punc(".",sen)
    sen = punc(",",sen)
    sen = punc("!",sen)
    return sen


def convSentence(sen):
    sen = spac(sen)
    sen = sen.split()
    smth = ''
    for i in range(len(sen)):
        sen[i] = pigLatin(sen[i])
        smth += sen[i]+' '
    smth = smth.swapcase()
    return smth


print convSentence("hey, how are you?")
