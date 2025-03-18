def xxor(x, y):
    return not(x == y)

x, y = map(int, input().split())
print(1 if xxor(x, y) else 0)