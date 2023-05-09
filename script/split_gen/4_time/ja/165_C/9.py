def dfs(A, N, M, Q, query, start, end, score):
    if len(A) == N:
        score = max(score, calc_score(A, query))
        return score
    for i in range(start, end + 1):
        A.append(i)
        score = dfs(A, N, M, Q, query, i, end, score)
        A.pop()
    return score
