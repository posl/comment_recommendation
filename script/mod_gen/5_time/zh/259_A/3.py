def solve(n,m,x,t,d):
    h = t
    for i in range(1,m):
        h += d
    for i in range(m,n):
        h += d
    return h

if __name__ == '__main__':
    solve()