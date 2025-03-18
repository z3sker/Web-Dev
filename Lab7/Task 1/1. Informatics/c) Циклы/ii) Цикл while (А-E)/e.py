n = int(input())
d = 1
c = 2
if n == 1:
    print(0)
    exit()
while c < n:
    c *= 2
    d += 1
print(d)