def problem137_b():
    K,X = map(int,input().split())
    for i in range(X-K+1,X+K):
        print(i,end=" ")
    print("")
problem137_b()
