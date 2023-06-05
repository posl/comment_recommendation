def get_score(A, B, C):
    score = 0
    for i in range(len(A)):
        score += B[A[i]-1]
        if i < len(A)-1:
            if A[i+1] == A[i] + 1:
                score += C[A[i]-1]
    return score

if __name__ == '__main__':
    get_score()