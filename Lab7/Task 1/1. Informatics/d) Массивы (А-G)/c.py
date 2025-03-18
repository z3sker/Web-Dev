n = int(input())
v = list(map(int, input().split()))
ans = 0
for i in range(n):
    if v[i] > 0:
        ans += 1
print(ans)