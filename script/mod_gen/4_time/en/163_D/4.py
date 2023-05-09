def main():
    N,K = map(int,input().split())
    mod = 10**9+7
    ans = 0
    for i in range(K,N+2):
        min_sum = i*(i-1)//2
        max_sum = i*(2*N-i+1)//2
        ans += (max_sum-min_sum+1)%mod
    print(ans%mod)

if __name__ == '__main__':
    main()