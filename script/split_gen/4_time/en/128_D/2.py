def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            l = V[:i]
            r = V[N-j:]
            l.sort()
            r.sort()
            for k in range(min(K - i - j, min(i, j))):
                if l[k] < 0 and r[min(K - i - j - k - 1, len(r) - 1)] < 0:
                    l[k], r[min(K - i - j - k - 1, len(r) - 1)] = r[min(K - i - j - k - 1, len(r) - 1)], l[k]
            ans = max(ans, sum(l) + sum(r))
    print(ans)
main()
