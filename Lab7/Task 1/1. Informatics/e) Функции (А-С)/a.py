def nmin(a, b, c, d):
    x = a
    if b < x:
        x = b
    if d < x:
        x = d
    if c < x:
        x = c
    return x


a, b, c, d = map(int, input().split())
ans = nmin(a, b, c, d)
print(ans)