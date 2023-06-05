def solve(n,m,t,a,x,y):
    for i in range(0,m):
        if t<=x[i]:
            return False
        else:
            t+=y[i]
    return True

if __name__ == '__main__':
    solve()