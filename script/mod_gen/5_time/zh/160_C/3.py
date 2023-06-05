def solve(k,n,alist):
    if n==1:
        return k
    else:
        return min(alist[i+1]-alist[i] for i in range(n-1))+k-alist[-1]+alist[0]

if __name__ == '__main__':
    solve()