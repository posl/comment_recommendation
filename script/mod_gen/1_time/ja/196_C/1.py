def check(x):
    s = str(x)
    n = len(s)
    for i in range(n//2):
        if s[i] != s[i+n//2]:
            return False
    return True
N = int(input())
ans = 0
for i in range(1,N+1):
    if check(i):
        ans += 1
print(ans)

if __name__ == '__main__':
    check()