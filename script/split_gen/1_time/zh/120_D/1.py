def main():
    N,M=map(int,input().split())
    A=[0]*M
    B=[0]*M
    for i in range(M):
        A[i],B[i]=map(int,input().split())
    #print(A)
    #print(B)
    ans=0
    for i in range(M):
        ans+=i*(N-i)*(B[i]-A[i])
    print(ans)
