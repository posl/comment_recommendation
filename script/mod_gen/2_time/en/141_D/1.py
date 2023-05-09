def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i]
        if i < m:
            ans = ans // 2
    print(ans)

if __name__ == '__main__':
    main()