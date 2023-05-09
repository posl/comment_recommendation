def solve(N,K,x):
    # write your code in Python 3.6
    ans = 10**20
    for i in range(N-K+1):
        ans = min(ans, abs(x[i])+abs(x[i+K-1]-x[i]), abs(x[i+K-1])+abs(x[i+K-1]-x[i]))
    return ans
