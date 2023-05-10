def dfs(A, count, N, M, Q, ans, abcd):
    if count == N:
        ans = max(ans, sum(abcd[i][3] for i in range(Q) if A[abcd[i][1]-1]-A[abcd[i][0]-1]==abcd[i][2]))
        return ans
    for i in range(A[-1], M+1):
        A.append(i)
        ans = dfs(A, count+1, N, M, Q, ans, abcd)
        A.pop()
    return ans

if __name__ == '__main__':
    dfs()