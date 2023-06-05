def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a,b,k=map(int,input().split())
c=gcd(a,b)
d=1
for i in range(c,0,-1):
    if c%i==0:
        d+=1
    if d==k+1:
        print(i)
        break

if __name__ == '__main__':
    gcd()