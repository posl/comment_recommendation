def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(A)
    #print(N)
    #print(K)
    #print(len(A))
    s = 0
    r = 0
    ans = 0
    for l in range(N):
        while r < N and s < K:
            s += A[r]
            r += 1
        if s < K:
            break
        ans += N-r+1
        if l == r:
            r += 1
        else:
            s -= A[l]
    print(ans)

if __name__ == '__main__':
    main()