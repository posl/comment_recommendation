def rec(a):
    if len(a)==N:
        print(*a)
        return
    if len(a)==0:
        for i in range(1,M+1):
            rec(a+[i])
    else:
        for i in range(a[-1],M+1):
            rec(a+[i])
N,M=map(int,input().split())
rec([])
