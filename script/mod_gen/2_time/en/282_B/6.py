def solve(N, M, S):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if all([S[i][k] == 'o' or S[j][k] == 'o' for k in range(M)]):
                count += 1
    return count

if __name__ == '__main__':
    solve()