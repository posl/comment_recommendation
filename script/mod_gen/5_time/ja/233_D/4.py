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
        if sum >= K:
            ans += N-r+1
        sum -= A[l]
    print(ans)
main()

if __name__ == '__main__':
    main()