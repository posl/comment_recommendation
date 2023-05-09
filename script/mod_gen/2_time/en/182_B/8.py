def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
N=int(input())
A=list(map(int,input().split()))
A.sort()
M=max(A)
G=[0]*(M+1)
for i in range(N):
    for j in range(2,M+1):
        if A[i]%j==0:
            G[j]+=1
print(G.index(max(G)))

if __name__ == '__main__':
    gcd()