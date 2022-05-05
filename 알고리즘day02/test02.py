n,m=map(int, input().split())

b=[list(map(int, input().split())) for i in range(n)]

total = 0

for i in range(3):
    for j in range(3):
        total += b[i][j]
        
print(total)