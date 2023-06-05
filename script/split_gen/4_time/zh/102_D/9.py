def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    B = [0 for i in range(N)]
    C = [0 for i in range(N)]
    D = [0 for i in range(N)]
    E = [0 for i in range(N)]
    B[0] = A[0]
    C[0] = A[1]
    D[0] = A[2]
    E[0] = A[3] + A[4]
    for i in range(1, N):
        B[i] = B[i-1] + A[i]
        if i >= 2:
            C[i] = C[i-1] + A[i]
        if i >= 3:
            D[i] = D[i-1] + A[i]
        if i >= 4:
            E[i] = E[i-1] + A[i]
    #print(B)
    #print(C)
    #print(D)
    #print(E)
    ans = 10**9
    for i in range(1, N-2):
        #print(i)
        for j in range(i+1, N-1):
            #print(j)
            for k in range(j+1, N):
                #print(k)
                p = B[i-1]
                q = C[j-1] - C[i-1]
                r = D[k-1] - D[j-1]
                s = E[N-1] - E[k-1]
                #print(p, q, r, s)
                ans = min(ans, max(p, q, r, s) - min(p, q, r, s))
    print(ans)
