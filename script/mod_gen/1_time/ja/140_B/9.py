def get_score(N, A, B, C):
    score = 0
    for i in range(N):
        score += B[A[i]-1]
        if i < N-1 and A[i] == A[i+1]-1:
            score += C[A[i]-1]
    return score

if __name__ == '__main__':
    get_score()