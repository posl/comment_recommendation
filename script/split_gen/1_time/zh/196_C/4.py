def check(x):
    s = str(x)
    l = len(s)
    if l % 2 == 1:
        return False
    for i in range(l//2):
        if s[i] != s[i+l//2]:
            return False
    return True
n = int(input())
ans = 0
for i in range(1,n+1):
    if check(i):
        ans += 1
print(ans)
