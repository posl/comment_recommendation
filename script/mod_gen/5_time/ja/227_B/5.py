def check(s):
    for a in range(1, 1001):
        for b in range(1, 1001):
            if s == 4*a*b+3*a+3*b:
                return True
    return False
n = int(input())
s = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if not check(s[i]):
        cnt += 1
print(cnt)

if __name__ == '__main__':
    check()