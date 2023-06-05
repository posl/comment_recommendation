def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1] % 2 == 0:
        print(a[-1])
        return
    for i in range(n-1):
        if a[i] % 2 == 0:
            print(a[i])
            return
    print(-1)

if __name__ == '__main__':
    main()