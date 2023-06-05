def dfs(A, N, M, Q, score, a, b, c, d):
    if a == N:
        print(A, score)
        return score
    else:
        for i in range(b-a+1):
            if A[a+i] == 0:
                A[a+i] = 1
                score += dfs(A, N, M, Q, score, a, b, c, d)
                A[a+i] = 0
            else:
                score += dfs(A, N, M, Q, score, a, b, c, d)
    return score

if __name__ == '__main__':
    dfs()