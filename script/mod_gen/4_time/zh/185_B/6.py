def solution():
    N,M,T = map(int,input().split())
    time = [0]*(T+1)
    for i in range(M):
        A,B = map(int,input().split())
        for j in range(A,B):
            time[j] += 1
    for i in range(T):
        if time[i]>0:
            N += 1
        else:
            N -= 1
        if N<=0:
            print("No")
            return
    print("Yes")
    return
solution()
