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
        score = [0]*M
        for j in range(N):
            if (i>>j)%2 == 1:
                cost += C[j]
                for k in range(M):
                    score[k] += A[j][k]
        if min(score) >= X:
            ans = min(ans,cost)
    if ans == 10**9:
        print(-1)
    else:
        print(ans)
