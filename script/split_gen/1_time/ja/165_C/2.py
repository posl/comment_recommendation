def main():
    n,m,q = map(int,input().split())
    a = [0] * q
    b = [0] * q
    c = [0] * q
    d = [0] * q
    for i in range(q):
        a[i],b[i],c[i],d[i] = map(int,input().split())
    ans = 0
    def dfs(A):
        nonlocal ans
        if len(A) == n:
            score = 0
            for i in range(q):
                if A[b[i]-1] - A[a[i]-1] == c[i]:
                    score += d[i]
            ans = max(ans,score)
            return
        A.append(A[-1])
        while A[-1] <= m:
            dfs(A)
            A[-1] += 1
        A.pop()
    dfs([1])
    print(ans)
