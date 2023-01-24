n = input("Enter phrase to be decrypted: ")
num = int(input("Enter the numeric decryption key: "))

spli = n.split()
joi = "".join(spli)

init = []

for i in joi:
    init.append(ord(i))

uncode = ""

for i in init:
    i = chr(i - num)
    uncode = uncode + i

print(uncode)
