n = int(input())
v = list(map(int, input().split()))
for i in range(n):
    if v[i] % 2 == 0:
        print(v[i])