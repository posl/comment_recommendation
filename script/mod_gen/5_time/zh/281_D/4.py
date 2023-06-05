def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(k):
        ans += a[i]
    if ans % d == 0:
        print(ans)
        return
    for i in range(k, n):
        ans += a[i]
        ans -= a[i-k]
        if ans % d == 0:
            print(ans)
            return
    print(-1)
    return

if __name__ == '__main__':
    main()