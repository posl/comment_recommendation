def check(n, m, s, c):
    if n > 3 or n < 1:
        print(-1)
        return
    if m > 5 or m < 0:
        print(-1)
        return
    if len(s) != m or len(c) != m:
        print(-1)
        return
    for i in range(m):
        if s[i] > n or s[i] < 1:
            print(-1)
            return
        if c[i] > 9 or c[i] < 0:
            print(-1)
            return
    if n == 1:
        print(c[0])
        return
    if n == 2:
        if s[0] == 1:
            print(c[0] * 10 + c[1])
            return
        else:
            print(c[1] * 10 + c[0])
            return
    if n == 3:
        if s[0] == 1:
            print(c[0] * 100 + c[1] * 10 + c[2])
            return
        elif s[0] == 2:
            print(c[1] * 100 + c[0] * 10 + c[2])
            return
        else:
            print(c[1] * 100 + c[2] * 10 + c[0])
            return

if __name__ == '__main__':
    check()