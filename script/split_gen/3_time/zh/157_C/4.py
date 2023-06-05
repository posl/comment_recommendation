def main():
    N, M = map(int, input().split())
    s = []
    c = []
    for i in range(M):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)
    if N == 1:
        if M == 1:
            print(c[0])
        else:
            print(-1)
    elif N == 2:
        if M == 1:
            if s[0] == 1:
                print(c[0] * 10)
            else:
                print(c[0])
        elif M == 2:
            if s[0] == 1:
                print(c[0] * 10 + c[1])
            elif s[0] == 2:
                print(c[1] * 10 + c[0])
            else:
                print(-1)
        else:
            print(-1)
    else:
        if M == 1:
            if s[0] == 1:
                print(c[0] * 100)
            elif s[0] == 2:
                print(c[0] * 10)
            elif s[0] == 3:
                print(c[0])
            else:
                print(-1)
        elif M == 2:
            if s[0] == 1:
                if s[1] == 2:
                    print(c[0] * 100 + c[1] * 10)
                elif s[1] == 3:
                    print(c[0] * 100 + c[1])
                else:
                    print(-1)
            elif s[0] == 2:
                if s[1] == 1:
                    print(c[1] * 100 + c[0] * 10)
                elif s[1] == 3:
                    print(c[1] * 10 + c[0])
                else:
                    print(-1)
            elif s[0] == 3:
                if s[1] == 1:
                    print(c[1] * 100 + c[0])
                elif s[1] == 2:
                    print(c[1] * 10 + c[0])
                else:
                    print(-1)
            else:
                print(-1)
        elif M == 3:
