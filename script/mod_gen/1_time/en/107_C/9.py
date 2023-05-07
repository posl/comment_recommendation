def main():
    #input
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    #compute
    if K == 1:
        print(0)
    else:
        ans = 10**9
        for i in range(N-K+1):
            left = X[i]
            right = X[i+K-1]
            if left*right <= 0:
                ans = min(ans, abs(left)+abs(right)+min(abs(left), abs(right)))
            else:
                ans = min(ans, max(abs(left), abs(right)))
        print(ans)

if __name__ == '__main__':
    main()