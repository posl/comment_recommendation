def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            l = V[:i] + V[N - j:]
            l.sort()
            ans = max(ans, sum(l[max(K - i - j, 0):]))
    print(ans)

if __name__ == '__main__':
    main()