def main():
    N, K = map(int, input().split())
    Vs = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) + 1):
            if i + j > K:
                continue
            if i + j > N:
                continue
            tmp = Vs[:i] + Vs[N - j:]
            tmp.sort()
            tmp = tmp[:K - i - j]
            ans = max(ans, sum(tmp))
    print(ans)

if __name__ == '__main__':
    main()