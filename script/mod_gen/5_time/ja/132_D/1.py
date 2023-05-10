def main():
    N, K = map(int, input().split())
    mod = 10**9+7
    ans = [0]*K
    for i in range(1, K+1):
        ans[i-1] = i
    for i in range(2, K+1):
        ans[i-1] += ans[i-2]
    for i in range(K, N):
        ans.append(ans[i-1]*i - ans[i-K-1]*(i-K))
    print(ans[N-1]%mod)

if __name__ == '__main__':
    main()