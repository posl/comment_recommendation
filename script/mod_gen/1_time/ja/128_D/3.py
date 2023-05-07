def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N - i, K - i) + 1):
            if i + j == 0:
                continue
            A = V[:i]
            B = V[N - j:]
            C = sorted(A + B)
            ans = max(ans, sum(C[max(0, i + j - K):]))
    print(ans)

if __name__ == '__main__':
    main()