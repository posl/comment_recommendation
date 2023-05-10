def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N,K)+1):
        for j in range(min(N,K)-i+1):
            t = V[:i] + V[N-j:]
            t.sort()
            for k in range(min(K-i-j, len(t))):
                if t[k] < 0:
                    t[k] = 0
            ans = max(ans, sum(t))
    print(ans)

if __name__ == '__main__':
    solve()