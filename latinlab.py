def pigLatin (pig):
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

def convSentence(sen):
    sen = sen.split()
    smth = ''
    for i in range(len(sen)):
        sen[i] = pigLatin(sen[i])
        smth += sen[i]+' '
    smth = smth.swapcase()
    return smth
