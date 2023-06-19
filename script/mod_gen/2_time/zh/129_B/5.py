def problems129_b():
    N=int(input())
    W=list(map(int,input().split()))
    min_diff=10000
    for i in range(N):
        S1=sum(W[:i+1])
        S2=sum(W[i+1:])
        if abs(S1-S2)<min_diff:
            min_diff=abs(S1-S2)
    print(min_diff)
problems129_b()
