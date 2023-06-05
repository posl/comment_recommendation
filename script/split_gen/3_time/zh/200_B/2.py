def myfun():
    N,K = input().split()
    N = int(N)
    K = int(K)
    for i in range(K):
        if N % 200 == 0:
            N = int(N / 200)
        else:
            N = int(str(N) + "200")
    print(N)
myfun()
