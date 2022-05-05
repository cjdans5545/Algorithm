a = [1,2,3]
b= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]#2차원 리스트 리스트 안에 리스트가 있는 것, 행렬이다.

print(a[2])
print(b[2][2])

#2중 for문으로 2차원리스트를 반복시킨다.
total=0
for i in range(3):
    for j in range(3):#i가 0일떄 j는 012
        total += b[i][j]
print(total)

