def main():
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0]*N
    S[0] = A[0]
    for i in range(1, N):
        S[i] = S[i-1] + A[i]
    d = dict()
    d[0] = 1
    ans = 0
    for i in range(N):
        if S[i] - K in d:
            ans += d[S[i] - K]
        if S[i] in d:
            d[S[i]] += 1
        else:
            d[S[i]] = 1
    print(ans)

if __name__ == '__main__':
    main()