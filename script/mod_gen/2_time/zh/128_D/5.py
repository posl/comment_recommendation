def solve(N,K,V):
    ans = 0
    for l in range(min(N,K)+1):
        for r in range(min(N,K)-l+1):
            s = 0
            t = []
            for i in range(l):
                s += V[i]
                t.append(V[i])
            for i in range(r):
                s += V[N-1-i]
                t.append(V[N-1-i])
            t.sort()
            for i in range(min(K-l-r,l+r)):
                if t[i] < 0:
                    s -= t[i]
            ans = max(ans,s)
    return ans
N,K = map(int,input().split())
V = list(map(int,input().split()))
print(solve(N,K,V))
