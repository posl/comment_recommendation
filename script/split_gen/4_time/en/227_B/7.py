def check(n, s):
    for a in range(1, n):
        for b in range(1, n):
            if 4 * a * b + 3 * a + 3 * b == s:
                return True
    return False
n = int(input())
s = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if not check(s[i], s[i]):
        cnt += 1
print(cnt)
