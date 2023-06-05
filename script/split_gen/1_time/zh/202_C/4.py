def count_same_num(N, A, B, C):
    # 暴力法
    count = 0
    for i in range(N):
        for j in range(N):
            if A[i] == B[C[j]-1]:
                count += 1
    return count
