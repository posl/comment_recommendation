def f(N,M):
    if N == 1:
        for i in range(1,M+1):
            print(i)
    else:
        for i in range(1,M+1):
            f(N-1,M-i)
            print(i)
f(3,5)
