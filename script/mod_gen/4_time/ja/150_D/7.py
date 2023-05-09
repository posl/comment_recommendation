def gcd(a,b):
    if a%b==0:
        return(b)
    else:
        return(gcd(b,a%b))
N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
A=list(set(A))
A.sort()
A.reverse()
B=[]
B.append(A[0])
for i in range(1,len(A)):
    if gcd(B[-1],A[i])==B[-1]:
        continue
    else:
        B.append(A[i])
A=B
#print(A)
ans=0
for i in range(len(A)):
    ans+=M//(2*A[i])
    ans-=M//(2*A[i])*2
print(ans)

if __name__ == '__main__':
    gcd()