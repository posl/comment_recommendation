def solve(N,K):
    ans = 0
    for i in range(K,N+2):
        ans += i*N-i*(i-1)//2+(i-1)*i//2+1
        ans %= 10**9+7
    return ans
