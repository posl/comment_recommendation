def main():
    n, m = map(int, input().split())
    s = []
    c = []
    for i in range(m):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)
    if n == 1:
        if m == 0:
            print(0)
        else:
            if s[0] == 1:
                print(c[0])
            else:
                print(-1)
    elif n == 2:
        if m == 0:
            print(10)
        elif m == 1:
            if s[0] == 1:
                print(c[0] * 10)
            else:
                print(-1)
        else:
            if s[0] == 1 and s[1] == 2:
                if c[0] == c[1]:
                    print(c[0] * 10 + c[1])
                else:
                    print(-1)
            else:
                print(-1)
    else:
        if m == 0:
            print(100)
        elif m == 1:
            if s[0] == 1:
                print(c[0] * 100)
            elif s[0] == 2:
                print(c[0] * 10 + 0)
            else:
                print(-1)
        elif m == 2:
            if s[0] == 1 and s[1] == 2:
                if c[0] == c[1]:
                    print(c[0] * 100 + c[1] * 10)
                else:
                    print(-1)
            elif s[0] == 1 and s[1] == 3:
                if c[0] == c[1]:
                    print(c[0] * 100 + c[1])
                else:
                    print(-1)
            elif s[0] == 2 and s[1] == 3:
                if c[0] == c[1]:
                    print(c[0] * 10 + c[1])
                else:
                    print(-1)
            else:
                print(-1)
        else:
            if s[0] == 1 and s[1] == 2 and s[2] == 3:
                if c[0] == c[
