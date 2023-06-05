def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
n,x=map(int,raw_input().split())
a=map(int,raw_input().split())
a.sort()
ans=abs(x-a[0])
for i in range(1,n):
    ans=gcd(ans,abs(x-a[i]))
print ans

if __name__ == '__main__':
    gcd()