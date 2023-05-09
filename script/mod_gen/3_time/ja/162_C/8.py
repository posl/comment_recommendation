def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)
K = int(input())
S = 0
for a in range(1,K+1):
    for b in range(1,K+1):
        for c in range(1,K+1):
            S += gcd(gcd(a,b),c)
print(S)

if __name__ == '__main__':
    gcd()