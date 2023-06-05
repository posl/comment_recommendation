def solve():
    N = int(input())
    A = [0]*N
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        A[i] = int(input())
        for j in range(A[i]):
            x,y = map(int,input().split())
            X[i] |= (1<<(x-1))
            Y[i] |= (y<<(x-1))
    #print(A)
    #print(X)
    #print(Y)
    ans = 0
    for i in range(1<<N):
        flag = True
        for j in range(N):
            if i & (1<<j):
                if (i & X[j]) != Y[j]:
                    flag = False
        if flag:
            ans = max(ans,bin(i).count("1"))
    print(ans)
