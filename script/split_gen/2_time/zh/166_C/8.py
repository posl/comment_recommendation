def problems166_c():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = list()
    B = list()
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        flag = True
        for j in range(M):
            if i+1 == A[j] and H[i] <= H[B[j]-1]:
                flag = False
            if i+1 == B[j] and H[i] <= H[A[j]-1]:
                flag = False
        if flag:
            ans += 1
    print(ans)
problems166_c()
