def check_honesty(honest_list, N, A, xy_list):
    for i in range(N):
        if honest_list[i] == 1:
            for j in range(A[i]):
                if honest_list[xy_list[i][j][0]-1] != xy_list[i][j][1]:
                    return False
    return True
