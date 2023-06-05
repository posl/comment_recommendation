def main():
    N,K = map(int,input().split())
    p = list(map(int,input().split()))
    sum_p = [0]*(N+1)
    for i in range(N):
        sum_p[i+1] = sum_p[i] + p[i]
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, (sum_p[i+K]-sum_p[i])/2 + sum_p[i])
    print(ans)

if __name__ == '__main__':
    main()