def find_min_time(N, S):
    min_time = 0
    for i in range(N):
        for j in range(N):
            if S[i][j] != S[0][j]:
                min_time += 1
    return min_time
