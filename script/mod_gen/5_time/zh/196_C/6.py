def check(x):
    s = str(x)
    l = len(s)
    if l % 2 == 1:
        return False
    for i in range(l // 2):
        if s[i] != s[l // 2 + i]:
            return False
    return True
N = int(input())
ans = 0
for i in range(1, N + 1):
    if check(i):
        ans += 1
print(ans)

if __name__ == '__main__':
    check()