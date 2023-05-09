def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(0, min(N, K) + 1):
        for r in range(0, min(N, K) - l + 1):
            if l + r > N or l + r > K:
                continue
            d = V[:l] + V[N - r:]
            d.sort()
            for i in range(min(K - l - r, len(d))):
                if d[i] < 0:
                    d[i] = 0
            ans = max(ans, sum(d))
    print(ans)

if __name__ == '__main__':
    main()