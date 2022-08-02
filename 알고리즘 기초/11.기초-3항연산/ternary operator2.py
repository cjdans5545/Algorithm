a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = (a if (a<=b) else b) if ((b if (b<=a) else a) <= c) else c
print (d)