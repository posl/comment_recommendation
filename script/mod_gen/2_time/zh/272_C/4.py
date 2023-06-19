def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n == 2:
        if a[0] % 2 == 0:
            print(a[0] + a[1])
        else:
            print(-1)
    else:
        if a[0] % 2 == 0:
            print(a[0] + a[1])
        else:
            print(a[-1] + a[-2])

if __name__ == '__main__':
    main()