def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
N,M=map(int,input().split())
A=[0]*N
A[0]=M
for i in range(1,N):
    A[i]=int(input())
A.sort()
ans=A[0]
for i in range(1,N):
    ans=gcd(ans,A[i])
print(ans)

if __name__ == '__main__':
    gcd()