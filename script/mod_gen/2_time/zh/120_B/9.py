def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a,b,k=map(int,input().split())
g=gcd(a,b)
l=[]
for i in range(1,g+1):
    if g%i==0:
        l.append(i)
print(l[-k])

if __name__ == '__main__':
    gcd()