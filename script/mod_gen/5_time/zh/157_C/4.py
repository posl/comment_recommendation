def main():
    n,m = map(int,input().split())
    s = []
    c = []
    for i in range(m):
        s1,c1 = map(int,input().split())
        s.append(s1)
        c.append(c1)
    if n == 1:
        print(c[0])
    elif n == 2:
        if s[0] == 1 and c[0] == 0:
            print(-1)
        else:
            print(c[0]*10+c[1])
    elif n == 3:
        if s[0] == 1 and c[0] == 0:
            if s[1] == 2 and c[1] == 0:
                print(-1)
            else:
                print(c[1]*100+c[2])
        elif s[0] == 1 and c[0] != 0:
            print(c[0]*100+c[1]*10+c[2])
        elif s[0] == 2 and c[0] == 0:
            if s[1] == 2 and c[1] == 0:
                print(-1)
            else:
                print(c[1]*10+c[2])
        elif s[0] == 2 and c[0] != 0:
            print(c[0]*10+c[1]*100+c[2])

if __name__ == '__main__':
    main()