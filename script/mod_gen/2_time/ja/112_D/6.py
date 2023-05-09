def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
N,M=map(int,input().split())
a=[]
for i in range(1,M//N+1):
    a.append(i)
#print(a)
ans=0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        ans=max(ans,gcd(a[i],a[j]))
print(ans)

if __name__ == '__main__':
    gcd()