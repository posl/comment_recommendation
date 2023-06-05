def solve(N,X,Y):
    if N == 1:
        return 0
    elif N == 2:
        return 1
    else:
        return solve(N-1,X,Y) + solve(N-2,X,Y) + X

if __name__ == '__main__':
    solve()