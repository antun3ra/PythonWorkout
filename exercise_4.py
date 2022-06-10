def hex_output():
    decnum = 0 
    hexnum = input('Please, enter a hex number to convert into decimal: ')
    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 ** power)
    print(decnum)

hex_output()