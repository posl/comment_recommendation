def get_max_num(N, A):
    max = 0
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            if i == 0:
                max = max * 10 + A[i][j]
                continue
            if j == 0:
                max = max * 10 + A[i][j]
                continue
            if i == N - 1:
                max = max * 10 + A[i][j]
                continue
            if j == N - 1:
                max = max * 10 + A[i][j]
                continue
            max = max * 10 + A[i][j]
    return max

if __name__ == '__main__':
    get_max_num()