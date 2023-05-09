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
            print(10, 11)
        elif M == 1:
            if s[0] == 1:
                if c[0] == 0:
                    print(10)
                else:
                    print(10 * c[0] + 1, 10 * c[0] + 10 + 1)
            else:
                print(-1)
        else:
            if s[0] == 1:
                if c[0] == 0:
                    if s[1] == 2:
                        print(10 * c[1] + 10)
                    else:
                        print(-1)
                else:
                    if s[1] == 2:
                        print(10 * c[0] + 10 * c[1] + 10)
                    else:
                        print(-1)
            else:
                print(-1)
    else:
        if M == 0:
            print(100, 101, 110, 111)
        elif M == 1:
            if s[0] == 1:
                if c[0] == 0:
                    print(100, 101, 110, 111)
                else:
                    print(100 * c[0] + 10, 100 * c[0] + 10 + 1, 100 * c[0] + 10 + 10, 100 * c[0] + 10 + 10 + 1)
            elif s[0] == 2:
                print(100 + 10 * c[0], 100 + 10 * c[0] + 1, 100 + 10 * c[0] + 10, 100 + 10 * c[0] + 10 + 1)
            elif s[0] == 3:

if __name__ == '__main__':
    main()