def main():
    N,M,X = map(int,input().split())
    C = []
    A = []
    for i in range(N):
        c,a = map(int,input().split())
        C.append(c)
        A.append(a)
    ans = 10**9
    for i in range(2**N):
        cost = 0
        understand = [0]*M
        for j in range(N):
            if (i>>j)&1:
                cost += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        if all(X <= u for u in understand):
            ans = min(ans,cost)
    if ans == 10**9:
        print(-1)
    else:
        print(ans)
