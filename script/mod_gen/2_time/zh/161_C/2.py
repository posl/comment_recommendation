def solve(n,k):
    if k==1:
        return 0
    if n<k:
        return min(n,abs(n-k))
    return min(n%k,abs(n%k-k))

if __name__ == '__main__':
    solve()