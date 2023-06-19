def solve(n,k):
    if n == 0:
        return 0
    else:
        return min(n%k,k-n%k)
