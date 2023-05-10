def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
N,K = map(int,input().split())
print(min(N%K,K-N%K))
