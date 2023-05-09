def solve(N, P):
    Q = [0] * N
    for i in range(N):
        Q[P[i]-1] = i+1
    return Q

if __name__ == '__main__':
    solve()