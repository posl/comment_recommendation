def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_cum = [0] * (n + 1)
    b_cum = [0] * (m + 1)
    for i in range(n):
        a_cum[i + 1] = a_cum[i] + a[i]
    for i in range(m):
        b_cum[i + 1] = b_cum[i] + b[i]
    ans = 0
    for i in range(n + 1):
        if a_cum[i] > k:
            break
        j = bisect.bisect_right(b_cum, k - a_cum[i])
        ans = max(ans, i + j - 1)
    print(ans)

if __name__ == '__main__':
    main()