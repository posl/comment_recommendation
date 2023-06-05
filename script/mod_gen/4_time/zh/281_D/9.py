def main():
    n,k,d = map(int, input().split())
    a = list(map(int, input().split()))
    if k == 1:
        if a[0] % d == 0:
            print(0)
        else:
            print(-1)
        return
    if k == 2:
        if (a[0] + a[1]) % d == 0:
            print(0)
        else:
            print(-1)
        return
    if k == 3:
        if (a[0] + a[1] + a[2]) % d == 0:
            print(0)
        else:
            print(-1)
        return
    if k == 4:
        if (a[0] + a[1] + a[2] + a[3]) % d == 0:
            print(0)
        else:
            print(-1)
        return

if __name__ == '__main__':
    main()