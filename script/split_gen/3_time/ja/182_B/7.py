def main():
    N=int(input())
    A=list(map(int,input().split()))
    B=[0]*1001
    for i in range(N):
        B[A[i]]+=1
    M=0
    for i in range(2,1001):
        C=0
        for j in range(i,1001,i):
            C+=B[j]
        if M<C:
            M=C
            ans=i
    print(ans)
