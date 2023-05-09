def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
k = int(input())
ans = 0
for a in range(1,k+1):
    for b in range(1,k+1):
        temp = gcd(a,b)
        for c in range(1,k+1):
            ans += gcd(temp,c)
print(ans)

if __name__ == '__main__':
    gcd()