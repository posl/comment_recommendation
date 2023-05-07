def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N - M + 1):
        for j in range(i + M, N + 1):
            ans = max(ans, sum(range(M + 1)) * sum(A[i:j]))
    print(ans)

if __name__ == '__main__':
    main()