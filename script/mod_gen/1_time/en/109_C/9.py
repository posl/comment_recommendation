def solve(N,X,x):
    x.append(X)
    x.sort()
    D = x[1]-x[0]
    for i in range(1,N):
        D = gcd(D,x[i+1]-x[i])
    return D

if __name__ == '__main__':
    solve()