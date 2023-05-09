def fuses(N, A, B):
    #print(N, A, B)
    t = 0
    for i in range(N):
        t += A[i]/B[i]
    #print(t)
    t = t/2
    #print(t)
    d = 0
    for i in range(N):
        d += A[i]*min(1, t*B[i]/A[i])
    #print(d)
    return d
