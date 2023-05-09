def main():
    N=int(input())
    A=list(map(int,input().split()))
    Q=int(input())
    BC=[list(map(int,input().split())) for _ in range(Q)]
    #print(N,A,Q,BC)
    A_sum=sum(A)
    #print(A_sum)
    A_count=[0]*(10**5+1)
    for i in A:
        A_count[i]+=1
    #print(A_count)
    for i in range(Q):
        B,C=BC[i]
        A_sum+=A_count[B]*(C-B)
        A_count[C]+=A_count[B]
        A_count[B]=0
        print(A_sum)
