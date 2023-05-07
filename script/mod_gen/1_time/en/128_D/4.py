def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N - i, K - i) + 1):
            v = V[:i] + V[N - j:]
            v.sort()
            ans = max(ans, sum(v) + sum([0] + v[:K - i - j] if v[:K - i - j] else [0]))
    print(ans)

if __name__ == '__main__':
    main()