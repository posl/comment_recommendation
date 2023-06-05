def get_satisfaction_score(N, A, B, C):
    score = 0
    for i in range(N):
        score += B[A[i]-1]
        if i != N-1 and A[i] + 1 == A[i+1]:
            score += C[A[i]-1]
    return score
