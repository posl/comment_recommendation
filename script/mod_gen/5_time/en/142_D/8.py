def gcd(a,b):
    return a if b==0 else gcd(b,a%b)
A,B=map(int,input().split())
g=gcd(A,B)
c=1
for i in range(2,int(g**0.5)+1):
    if g%i==0:
        c+=1
        while g%i==0:
            g//=i

if __name__ == '__main__':
    gcd()