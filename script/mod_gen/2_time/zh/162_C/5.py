def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
K = int(input())
ans = 0
for i in range(1,K+1):
    for j in range(1,K+1):
        for k in range(1,K+1):
            ans += gcd(i,gcd(j,k))
print(ans)

if __name__ == '__main__':
    gcd()