def main():
    n,m = map(int,input().split())
    if n == 1:
        for i in range(m):
            s,c = map(int,input().split())
            if s == 1 and c == 0:
                print(0)
                return
            else:
                print(-1)
                return
    elif n == 2:
        for i in range(m):
            s,c = map(int,input().split())
            if s == 1 and c == 0:
                print(-1)
                return
            elif s == 2 and c == 0:
                print(-1)
                return
            elif s == 1 and c != 0:
                print(c*10)
                return
            elif s == 2 and c != 0:
                print(c)
                return
    elif n == 3:
        for i in range(m):
            s,c = map(int,input().split())
            if s == 1 and c == 0:
                print(-1)
                return
            elif s == 2 and c == 0:
                print(-1)
                return
            elif s == 3 and c == 0:
                print(-1)
                return
            elif s == 1 and c != 0:
                print(c*100)
                return
            elif s == 2 and c != 0:
                print(c*10)
                return
            elif s == 3 and c != 0:
                print(c)
                return

if __name__ == '__main__':
    main()