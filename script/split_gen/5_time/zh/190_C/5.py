def solve():
    N,M = map(int,input().split())
    A = []
    B = []
    for _ in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    K = int(input())
    C = []
    D = []
    for _ in range(K):
        c,d = map(int,input().split())
        C.append(c)
        D.append(d)
    ans = 0
    for i in range(1<<K):
        dish = [False]*N
        for j in range(K):
            if i & 1<<j:
                dish[C[j]-1] = True
            else:
                dish[D[j]-1] = True
        cnt = 0
        for j in range(M):
            if dish[A[j]-1] and dish[B[j]-1]:
                cnt += 1
        ans = max(ans,cnt)
    print(ans)
