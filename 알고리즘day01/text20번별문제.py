n = int(input())

for i in range(n):
    #1. 짝수 줄이니?
    if i % 2 ==0 :
        print("* " * n)
    #2. 홀수 줄이니?
    else:
        print(" *" * n)

"""
-------------------------------


n = int(input())
line = "* " * n

for i in range(n):
    print(line)
    line = line[::-1]
"""