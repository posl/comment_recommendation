def main():
    N, M = map(int, input().split())
    s = []
    c = []
    for i in range(M):
        a, b = map(int, input().split())
        s.append(a)
        c.append(b)
    if N == 1 and M == 0:
        print(0)
    elif N == 1 and M == 1:
        print(c[0])
    elif N == 1 and M > 1:
        print(-1)
    elif N == 2 and M == 0:
        print(10)
    elif N == 2 and M == 1:
        print(-1)
    elif N == 2 and M == 2:
        if s[0] == 1 and s[1] == 2:
            print(c[0]*10+c[1])
        elif s[0] == 2 and s[1] == 1:
            print(c[1]*10+c[0])
        else:
            print(-1)
    elif N == 2 and M > 2:
        print(-1)
    elif N == 3 and M == 0:
        print(100)
    elif N == 3 and M == 1:
        print(-1)
    elif N == 3 and M == 2:
        if s[0] == 1 and s[1] == 2:
            print(c[0]*100+c[1]*10)
        elif s[0] == 1 and s[1] == 3:
            print(c[0]*100+c[1])
        elif s[0] == 2 and s[1] == 1:
            print(c[1]*100+c[0]*10)
        elif s[0] == 2 and s[1] == 3:
            print(c[1]*100+c[0])
        elif s[0] == 3 and s[1] == 1:
            print(c[1]*100+c[0])
        elif s[0] == 3 and s[1] == 2:
            print(c[1]*100+c[0]*10)
        else:
            print(-1)
    elif N == 3 and M == 3:
        if s[0] == 1 and s[1] == 2 and s[2]

if __name__ == '__main__':
    main()