def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        if a[0] == 0:
            print(0)
        else:
            print(-1)
        return
    if a[0] == 1:
        print(-1)
        return
    if a[-1] == 0:
        print(-1)
        return
    if n == 2:
        if a[0] == a[1]:
            print(0)
            return
        else:
            print(-1)
            return
    if a[0] == 0 and a[1] == 0:
        print(-1)
        return
    if a[0] == 0 and a[1] == 1 and a[2] == 1:
        print(-1)
        return
    if a[0] == 0 and a[1] == 1 and a[2] == 0:
        a[0] = 1
        a[1] = 0
        a[2] = 1
    if a[0] == 1 and a[1] == 0 and a[2] == 0:
        a[0] = 0
        a[1] = 1
        a[2] = 1
    if a[0] == 1 and a[1] == 0 and a[2] == 1:
        a[0] = 0
        a[1] = 1
        a[2] = 0
    if a[0] == 1 and a[1] == 1 and a[2] == 0:
        a[0] = 0
        a[1] = 0
        a[2] = 1
    if a[0] == 1 and a[1] == 1 and a[2] == 1:
        a[0] = 0
        a[1] = 0
        a[2] = 0
    for i in range(3, n):
        if a[i] == 0:
            continue
        if a[i - 1] == 0 and a[i - 2] == 0:
            print(-1)

if __name__ == '__main__':
    main()