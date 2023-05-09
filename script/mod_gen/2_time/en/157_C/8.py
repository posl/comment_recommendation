def get_num(N, M, s, c):
    if M == 0:
        if N == 1:
            return 0
        else:
            return -1
    if N == 1:
        if M == 1 and s[0] == 1:
            return c[0]
        else:
            return -1
    if N == 2:
        if M == 1 and s[0] == 1:
            return c[0] * 10
        elif M == 1 and s[0] == 2:
            return c[0]
        else:
            return -1
    if N == 3:
        if M == 1 and s[0] == 1:
            return c[0] * 100
        elif M == 1 and s[0] == 2:
            return c[0] * 10
        elif M == 1 and s[0] == 3:
            return c[0]
        elif M == 2 and s[0] == 1 and s[1] == 2:
            return c[0] * 10 + c[1]
        elif M == 2 and s[0] == 1 and s[1] == 3:
            return c[0] * 100 + c[1] * 10
        elif M == 2 and s[0] == 2 and s[1] == 3:
            return c[0] * 10 + c[1]
        else:
            return -1

if __name__ == '__main__':
    get_num()