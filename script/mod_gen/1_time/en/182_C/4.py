def main():
    N = input()
    a = [int(i) for i in N]
    if sum(a) % 3 == 0:
        print(0)
        return
    if len(N) == 1:
        print(-1)
        return
    if len(N) == 2:
        if (a[0] + a[1]) % 3 == 0:
            print(1)
        else:
            print(-1)
        return
    if len(N) == 3:
        if (a[0] + a[1] + a[2]) % 3 == 0:
            print(0)
        elif (a[0] + a[1]) % 3 == 0 or (a[1] + a[2]) % 3 == 0 or (a[0] + a[2]) % 3 == 0:
            print(1)
        else:
            print(-1)
        return
    if len(N) == 4:
        if (a[0] + a[1] + a[2] + a[3]) % 3 == 0:
            print(0)
        elif (a[0] + a[1] + a[2]) % 3 == 0 or (a[1] + a[2] + a[3]) % 3 == 0 or (a[0] + a[1] + a[3]) % 3 == 0:
            print(1)
        elif (a[0] + a[1]) % 3 == 0 or (a[1] + a[2]) % 3 == 0 or (a[2] + a[3]) % 3 == 0 or (a[0] + a[2]) % 3 == 0 or (a[0] + a[3]) % 3 == 0 or (a[1] + a[3]) % 3 == 0:
            print(2)
        else:
            print(-1)
        return
    if len(N) == 5:
        if (a[0] + a[1] + a[2] + a[3] + a[4]) % 3 == 0:
            print(0)
        elif (a[0] + a

if __name__ == '__main__':
    main()