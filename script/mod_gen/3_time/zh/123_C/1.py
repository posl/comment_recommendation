def solve(N,A,B,C,D,E):
    #print(N,A,B,C,D,E)
    if N == 0:
        return 0
    else:
        return min(solve(N//A,A,B,C,D,E)+1, solve(N//B,A,B,C,D,E)+1, solve(N//C,A,B,C,D,E)+1, solve(N//D,A,B,C,D,E)+1, solve(N//E,A,B,C,D,E)+1)

if __name__ == '__main__':
    solve()