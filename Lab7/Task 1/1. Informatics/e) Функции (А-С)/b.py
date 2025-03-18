def stepen(a, b):
    return a ** b

a, b = input().split()
a = float(a)
b = int(b)
ans = stepen(a, b)
print(ans)