def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1] % 2 == 0:
        print(a[-1])
    else:
        for i in range(n-1, 0, -1):
            if a[i] % 2 == 0:
                print(a[i])
                break
            elif (a[i] + a[i-1]) % 2 == 0:
                print(a[i] + a[i-1])
                break
            elif i == 1:
                print(-1)

if __name__ == '__main__':
    main()