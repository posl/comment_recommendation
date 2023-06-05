def get_score(N, M, Q, lst):
    score = 0
    for i in range(N):
        for j in range(M):
            for k in range(Q):
                if lst[k][1] - lst[k][0] == lst[k][2]:
                    score += lst[k][3]
    return score

if __name__ == '__main__':
    get_score()