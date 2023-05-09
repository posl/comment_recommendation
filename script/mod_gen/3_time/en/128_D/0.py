def main():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    for i in range(min(n, k) + 1):
        for j in range(min(n, k) - i + 1):
            l = v[:i] + v[n - j:]
            l.sort()
            ans = max(ans, sum(l[max(0, k - i - j):]))
    print(ans)

if __name__ == '__main__':
    main()