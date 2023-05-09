def solve(N, M, k, x):
    #N: number of people
    #M: number of parties
    #k: k[i] is the number of people who attended the i-th party
    #x: x[i][j] is the j-th person who attended the i-th party
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for k_i in range(M):
                if i+1 in x[k_i] and j+1 in x[k_i]:
                    break
            else:
                return 'No'
    return 'Yes'

if __name__ == '__main__':
    solve()