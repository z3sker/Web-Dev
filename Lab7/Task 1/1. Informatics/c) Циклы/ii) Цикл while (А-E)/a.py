n = int(input())
x = 1
while True:
    if x * x <= n:
        print(x * x)
    else:
        break
    x = x + 1