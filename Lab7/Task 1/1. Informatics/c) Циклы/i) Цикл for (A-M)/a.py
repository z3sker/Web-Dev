a = int(input())
b = int(input())
if a % 2 != 0:
    a += 1
if b % 2 == 0:
    b += 1
for i in range(a, b, 2):
    print(i)