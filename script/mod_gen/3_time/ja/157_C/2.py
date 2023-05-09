def main():
    N, M = map(int, input().split())
    s = [0] * M
    c = [0] * M
    for i in range(M):
        s[i], c[i] = map(int, input().split())
    if N == 1:
        if M == 0:
            print(0)
        else:
            if s[0] == 1:
                print(c[0])
            else:
                print(-1)
    elif N == 2:
        if M == 0:
            print(10)
        elif M == 1:
            if s[0] == 1:
                print(c[0] * 10)
            elif s[0] == 2:
                print(c[0] + 10)
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
        if M == 0:
            print(100)
        elif M == 1:
            if s[0] == 1:
                print(c[0] * 100)
            elif s[0] == 2:
                print(c[0] * 10 + 100)
            elif s[0] == 3:
                print(c[0] + 100)
            else:
                print(-1)
        elif M == 2:
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
                    print(c[0] * 10 + c[1] + 100)
                else:
                    print(-1)
            else:

if __name__ == '__main__':
    main()