def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N - i, K - i) + 1):
            tmp = V[:i] + V[N - j:]
            tmp.sort()
            ans = max(ans, sum(tmp[max(0, K - i - j):]))
    print(ans)

if __name__ == '__main__':
    main()