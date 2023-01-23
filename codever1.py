import random

n = input("Enter phrase to encrypt here: ")
spli = n.split()
joi = "".join(spli)

init = []
crypt = []

for i in joi:
    init.append(ord(i))

code = ""

lol = random.randint(0, 256)

for i in init:
        i = chr(i + lol)
        code = code + i

print(code) 
