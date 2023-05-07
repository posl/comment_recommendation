def main():
    N,W=map(int,input().split())
    S=[0]*N
    T=[0]*N
    P=[0]*N
    for i in range(N):
        S[i],T[i],P[i]=map(int,input().split())
    S_max=max(S)
    T_max=max(T)
    #print(S_max,T_max)
    #print(S)
    #print(T)
    #print(P)
    #print(sum(P))
    if sum(P)>W:
        print("No")
        return
    else:
        for i in range(S_max,T_max):
            tmp=0
            for j in range(N):
                if S[j]<=i and i<T[j]:
                    tmp+=P[j]
            if tmp>W:
                print("No")
                return
        print("Yes")
