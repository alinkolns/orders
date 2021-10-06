from random import randint

rnd = randint(2, 3)
#print(rnd)

Symbol = ["о", "О","o", "O" ]
with open ("C.txt", "r") as myfile:
    data = myfile.read().replace('\n', '')
    print(data)
    freq = 0
    for char in data:
        if char == Symbol:
            freq = freq + 1
    print(freq)
