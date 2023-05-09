def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    V.reverse()
    ans = 0
    for i in range(min(K, N) + 1):
        for j in range(min(K, N) - i + 1):
            d = V[:i] + V[N - j:]
            d.sort()
            for k in range(min(K - i - j, len(d))):
                if d[k] < 0:
                    d[k] = 0
            ans = max(ans, sum(d))
    print(ans)

if __name__ == '__main__':
    main()