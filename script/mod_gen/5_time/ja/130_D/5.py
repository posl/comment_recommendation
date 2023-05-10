def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    sum = 0
    r = 0
    for l in range(N):
        while r < N and sum < K:
            sum += A[r]
            r += 1
        if sum < K:
            break
        ans += N-r+1
        if l == r:
            r += 1
        else:
            sum -= A[l]
    print(ans)

if __name__ == '__main__':
    main()