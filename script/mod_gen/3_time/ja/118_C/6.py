def gcd(a,b):
    if a%b==0:
        return(b)
    else:
        return(gcd(b,a%b))
n = int(input())
a = list(map(int,input().split()))
a.sort()
m = a[0]
for i in range(n):
    m = gcd(m,a[i])
print(m)

if __name__ == '__main__':
    gcd()