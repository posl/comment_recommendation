def solve(N, K, V):
    ans = 0
    for k in range(1, min(K, N)+1):
        for l in range(k+1):
            r = k-l
            tmp = sum(V[:l])+sum(V[N-r:])
            ans = max(ans, tmp+max(0, K-k))
    return ans

if __name__ == '__main__':
    solve()