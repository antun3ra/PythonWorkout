def pl_sentence(sent):
    sent = sent.split()
    for word in sent:
        if word[0].lower() in 'aeiou':
            print(word+'way ', end='',)
        else:
            print(word[1:]+word[0]+'ay ', end='')

pl_sentence('testing my awesome function')