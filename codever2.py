import random

n = input("Enter phrase to encrypt here: ")
bo = input("Enter Y/N for creating an entirely random code: ")
spli = n.split()
joi = "".join(spli)

init = []
crypt = []

for i in joi:
    init.append(ord(i))

code = ""

if bo == 'Y' or bo == 'y':
    lol = random.randint(0, 256)
    for i in init:
        i = chr(i + lol)
        code = code + i

elif bo == 'N' or bo == 'n':
    var = int(input("Enter the fixed length here: "))
    for i in init:
        i = chr(i + var)
        code = code + i
        print(code)

print(code) 
