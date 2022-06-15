def pig_latin(w):
    if w[0].lower() in 'aeiou':
        return w+'way'
    else:
        return w[1:]+w[0]+'ay'

print(pig_latin('world'))