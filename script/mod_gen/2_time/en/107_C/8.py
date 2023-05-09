def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = float("inf")
    for i in range(N-K+1):
        ans = min(ans, A[i+K-1] - A[i] + min(abs(A[i+K-1]), abs(A[i])))
    print(ans)

if __name__ == '__main__':
    main()