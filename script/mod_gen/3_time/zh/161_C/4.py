def solve(n,k):
    while n>=k:
        n=n%k
        if n==0:
            return 0
        elif n>k/2:
            n=k-n
    return n
n,k=map(int,input().split())
print(solve(n,k))
