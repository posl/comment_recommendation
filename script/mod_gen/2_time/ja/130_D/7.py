def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K)
    #print(A)
    ans = 0
    l = 0
    r = 0
    S = 0
    while l < N:
        while r < N and S < K:
            S += A[r]
            r += 1
        #print(l, r, S)
        if S >= K:
            ans += N - r + 1
        S -= A[l]
        l += 1
    print(ans)

if __name__ == '__main__':
    main()