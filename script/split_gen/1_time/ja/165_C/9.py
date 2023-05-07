def dfs(A, M, Q, abcd, index=0, score=0):
    if index == len(A):
        return score
    else:
        max_score = 0
        for i in range(A[index-1], M+1):
            A[index] = i
            tmp_score = score
            for j in range(Q):
                if A[abcd[j][1]-1] - A[abcd[j][0]-1] == abcd[j][2]:
                    tmp_score += abcd[j][3]
            max_score = max(max_score, dfs(A, M, Q, abcd, index+1, tmp_score))
        return max_score
