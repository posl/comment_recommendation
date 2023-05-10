def get_max_score(N,M,Q,query):
    ans = 0
    A = [1]*N
    while A[0] <= M:
        score = 0
        for i in range(Q):
            if A[query[i][1]-1] - A[query[i][0]-1] == query[i][2]:
                score += query[i][3]
        if score > ans:
            ans = score
        A[-1] += 1
        for i in range(N-1,0,-1):
            if A[i] > M:
                A[i] = 1
                A[i-1] += 1
    return ans

if __name__ == '__main__':
    get_max_score()