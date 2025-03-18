s = input()
ans = 0
d = 0
s = s[::-1]
for i in range(0, len(s)):
    ans += int(s[i]) * (2 ** d)
    d += 1
print(ans)
