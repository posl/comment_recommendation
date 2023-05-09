def dfs(A, N, M, Q, a, b, c, d):
    if len(A) == N:
        #print(A)
        return calc(A, Q, a, b, c, d)
    else:
        for i in range(A[-1], M+1):
            dfs(A+[i], N, M, Q, a, b, c, d)

if __name__ == '__main__':
    dfs()