def ubbi_dubbi(word):
    output = []
    for letter in word:
        if letter.lower() in 'aeiou':
            output.append('ub'+letter)
        else:
            output.append(letter)
    final_word = ''.join(output)
    return final_word

print(ubbi_dubbi('anonymous'))