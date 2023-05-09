def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = -float("inf")
    for i in range(N-M+1):
        for j in range(i+M, N+1):
            ans = max(ans, sum(A[i:j]) * M)
            M -= 1
    print(ans)

if __name__ == '__main__':
    main()