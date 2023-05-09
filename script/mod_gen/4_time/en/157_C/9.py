def main():
    n, m = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(m)]
    sc.sort()
    if n == 1:
        if m == 0:
            print(0)
        elif m == 1:
            print(sc[0][1])
        else:
            print(-1)
    elif n == 2:
        if m == 0:
            print(10)
        elif m == 1:
            print(sc[0][1] * 10)
        elif m == 2:
            if sc[0][0] == 1:
                print(sc[0][1] * 10 + sc[1][1])
            else:
                print(sc[0][1] + sc[1][1] * 10)
        else:
            print(-1)
    elif n == 3:
        if m == 0:
            print(100)
        elif m == 1:
            print(sc[0][1] * 100)
        elif m == 2:
            if sc[0][0] == 1:
                print(sc[0][1] * 100 + sc[1][1] * 10)
            elif sc[0][0] == 2:
                print(sc[0][1] * 100 + sc[1][1])
            else:
                print(-1)
        elif m == 3:
            if sc[0][0] == 1 and sc[1][0] == 2:
                print(sc[0][1] * 100 + sc[1][1] * 10 + sc[2][1])
            else:
                print(-1)
        else:
            print(-1)
    else:
        print(-1)

if __name__ == '__main__':
    main()