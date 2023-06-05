def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == 0:
        print(-1)
        return
    if n == 2:
        if a[0] == a[1]:
            print(-1)
            return
        else:
            print(a[0]+a[1])
            return
    if n == 3:
        if a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
            print(-1)
            return
        else:
            print(a[0]+a[1])
            return
    if n == 4:
        if a[0] == a[1] or a[0] == a[2] or a[0] == a[3] or a[1] == a[2] or a[1] == a[3] or a[2] == a[3]:
            print(-1)
            return
        else:
            print(a[0]+a[1])
            return
    if n == 5:
        if a[0] == a[1] or a[0] == a[2] or a[0] == a[3] or a[0] == a[4] or a[1] == a[2] or a[1] == a[3] or a[1] == a[4] or a[2] == a[3] or a[2] == a[4] or a[3] == a[4]:
            print(-1)
            return
        else:
            print(a[0]+a[1])
            return
    if n == 6:
        if a[0] == a[1] or a[0] == a[2] or a[0] == a[3] or a[0] == a[4] or a[0] == a[5] or a[1] == a[2] or a[1] == a[3] or a[1] == a[4] or a[1] == a[5] or a[2] == a[3] or a[2] == a[4] or a[2] == a[5] or a[

if __name__ == '__main__':
    main()