def calc_score(A,B):
    score = 0
    for i in range(Q):
        if A[B[i][1]-1] - A[B[i][0]-1] == B[i][2]:
            score += B[i][3]
    return score

if __name__ == '__main__':
    calc_score()