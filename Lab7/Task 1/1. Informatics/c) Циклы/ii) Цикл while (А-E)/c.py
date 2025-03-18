n = int(input())
x = 2
if 1 <= n:
    print(1)
if 2 <= n:
    print(2)
if 4 <= n:
    while True:
        x *= 2
        if x > n:
            break
        print(x)