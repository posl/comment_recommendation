def solve(N, M, s, c):
    #N: 位数
    #M: 条件数
    #s: 条件位置
    #c: 条件值
    #print(N, M, s, c)
    if N == 1:
        if M == 0:
            return 0
        elif M == 1:
            return c[0]
        else:
            return -1
    elif N == 2:
        if M == 0:
            return 0
        elif M == 1:
            if s[0] == 1:
                return c[0] * 10
            else:
                return c[0] + 10
        elif M == 2:
            if s[0] == 1:
                return c[0] * 10 + c[1]
            elif s[0] == 2:
                return c[1] * 10 + c[0]
            else:
                return -1
        else:
            return -1
    else:
        if M == 0:
            return 0
        elif M == 1:
            if s[0] == 1:
                return c[0] * 100
            elif s[0] == 2:
                return c[0] * 10
            else:
                return c[0]
        elif M == 2:
            if s[0] == 1 and s[1] == 2:
                return c[0] * 100 + c[1] * 10
            elif s[0] == 1 and s[1] == 3:
                return c[0] * 100 + c[1]
            elif s[0] == 2 and s[1] == 1:
                return c[1] * 100 + c[0] * 10
            elif s[0] == 2 and s[1] == 3:
                return c[1] * 10 + c[0]
            elif s[0] == 3 and s[1] == 1:
                return c[1] * 100 + c[0]
            elif s[0] == 3 and s[1] == 2:
                return c[1] * 10 + c

if __name__ == '__main__':
    solve()