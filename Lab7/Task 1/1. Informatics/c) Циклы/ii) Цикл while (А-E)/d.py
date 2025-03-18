n = int(input())
if n == 1:
    print("YES")
else:
    while n > 2:
        n = n / 2
    print("YES" if n == 2 else "NO")