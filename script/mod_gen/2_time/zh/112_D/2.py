def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
N,M=map(int,input().split())
i=1
ans=0
while i*i<=M:
    if M%i==0:
        if M//i>=N:
            ans=max(ans,i)
        if i>=N:
            ans=max(ans,M//i)
    i+=1
print(ans)

if __name__ == '__main__':
    gcd()