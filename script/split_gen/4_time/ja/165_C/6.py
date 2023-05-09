def dfs(A, N, M, Q, abcd, ans):
    if len(A) == N:
        sum = 0
        for i in range(Q):
            if A[abcd[i][1]-1] - A[abcd[i][0]-1] == abcd[i][2]:
                sum += abcd[i][3]
        ans[0] = max(ans[0], sum)
        return
    for i in range(A[-1], M+1):
        A.append(i)
        dfs(A, N, M, Q, abcd, ans)
        A.pop()
