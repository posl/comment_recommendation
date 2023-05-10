def check(s, n):
    for i in range(10):
        if s[i] == 'o':
            if not str(i) in n:
                return False
        elif s[i] == 'x':
            if str(i) in n:
                return False
    return True
s = input()
ans = 0
for i in range(10000):
    n = str(i).zfill(4)
    if check(s, n):
        ans += 1
print(ans)

if __name__ == '__main__':
    check()