def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    import math
    def gcd(a,b):
        if a<b:
            a,b = b,a
        while b!=0:
            a,b = b,a%b
        return a
    def lcm(a,b):
        return a*b//gcd(a,b)
    G = A[0]
    for i in range(1,N):
        G = gcd(G,A[i])
    if M%G!=0:
        print(0)
        return
    M = M//G
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(1,int(math.sqrt(M))+1):
        if M%i==0:
            d[i] = 1
            d[M//i] = 1
    d = sorted(d.items())
    ans = []
    for i in range(len(d)):
        if d[i][1]==1:
            ans.append(d[i][0]*G)
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i])

if __name__ == '__main__':
    main()