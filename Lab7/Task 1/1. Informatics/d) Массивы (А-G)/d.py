n = int(input())
v = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    if v[i] > v[i - 1]:
        ans += 1
print(ans)