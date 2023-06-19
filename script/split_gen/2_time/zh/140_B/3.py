def get_max_score(N, A, B, C):
    max_score = 0
    for i in range(N):
        score = 0
        score += B[A[i]-1]
        if i < N-1:
            score += C[A[i]-1]
        if score > max_score:
            max_score = score
    return max_score
