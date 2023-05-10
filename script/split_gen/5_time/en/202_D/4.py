def nCr(n,r):
    if n<r:
        return 0
    else:
        return fact[n]//fact[n-r]//fact[r]
fact=[1]*(61)
for i in range(2,61):
    fact[i]=i*fact[i-1]
A,B,K=map(int,input().split())
ans=""
for i in range(A+B):
    if A==0:
        ans+="b"
    elif B==0:
        ans+="a"
    elif K<=nCr(A+B-1,B):
        ans+="a"
        A-=1
    else:
        ans+="b"
        K-=nCr(A+B-1,B)
        B-=1
print(ans)
