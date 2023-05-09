def solve(X,Y,N):
    if N%3 == 0:
        return min(X*N//3,Y*N)
    elif N%3 == 1:
        return min(X*(N-1)//3+Y,X+N//3*Y)
    else:
        return min(X*(N-2)//3+2*Y,X+(N-2)//3*Y)

if __name__ == '__main__':
    solve()