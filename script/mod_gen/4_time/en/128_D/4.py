def main():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    for a in range(min(n, k) + 1):
        for b in range(min(n, k) + 1 - a):
            c = k - a - b
            d = v[:a] + v[n-b:]
            d.sort()
            ans = max(ans, sum(d[max(0, c - len(d)):]))
    print(ans)

if __name__ == '__main__':
    main()