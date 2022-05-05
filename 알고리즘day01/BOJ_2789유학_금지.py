from re import I


word = input()

for i in "CAMBRIDGE":
    word = word.replace(i, "")

print(word)

'''
for i in input():
    if not i in "CAMBRIDGE":
        print(end=i)
'''