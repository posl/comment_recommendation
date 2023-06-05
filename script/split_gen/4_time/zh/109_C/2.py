def main():
    N,X = map(int,input().split())
    x = list(map(int,input().split()))
    x.append(X)
    x.sort()
    d = [x[i+1] - x[i] for i in range(N)]
    import math
    def gcd(a,b):
        while b:
            a,b = b,a%b
        return a
    def lcm(a,b):
        return a*b//gcd(a,b)
    ans = d[0]
    for i in range(1,N):
        ans = gcd(ans,d[i])
    print(ans)
