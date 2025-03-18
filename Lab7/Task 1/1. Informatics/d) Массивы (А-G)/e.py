n = int(input())
v = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    if (v[i] >= 0 and v[i - 1] >= 0) or (v[i] <= 0 and v[i - 1] <= 0):
        ans += 1
print("YES" if ans else "NO")