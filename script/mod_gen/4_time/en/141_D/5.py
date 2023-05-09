def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] < 2**m:
            ans += a[i]
        else:
            ans += a[i] // 2**m
    print(ans)

if __name__ == '__main__':
    main()