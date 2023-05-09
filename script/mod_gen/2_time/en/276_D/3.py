def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] //= 2
            elif a[i] % 3 == 0:
                a[i] //= 3
            else:
                if a.count(a[0]) == n:
                    print(ans)
                    return
                else:
                    print(-1)
                    return
        ans += 1

if __name__ == '__main__':
    main()