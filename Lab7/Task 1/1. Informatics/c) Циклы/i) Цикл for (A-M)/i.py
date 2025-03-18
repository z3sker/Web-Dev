import math

a = int(input())
s = 0
for i in range(1, math.isqrt(a) + 1):
    if a % i == 0:
        s += 1
        if i * i != a:
            s += 1
print(s)