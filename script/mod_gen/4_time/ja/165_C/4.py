def dfs(A,N,M,Q):
    global ans
    if len(A) == N:
        score = 0
        for i in range(Q):
            if A[b[i]-1]-A[a[i]-1] == c[i]:
                score += d[i]
        ans = max(ans,score)
        return
    A.append(A[-1])
    while A[-1] <= M:
        dfs(A,N,M,Q)
        A[-1] += 1
    A.pop()
    return
N,M,Q = map(int,input().split())
a,b,c,d = [],[],[],[]
for i in range(Q):
    A,B,C,D = map(int,input().split())
    a.append(A)
    b.append(B)
    c.append(C)
    d.append(D)
ans = 0
dfs([1],N,M,Q)
print(ans)

if __name__ == '__main__':
    dfs()