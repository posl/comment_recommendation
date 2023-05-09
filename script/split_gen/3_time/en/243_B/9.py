def solve(N, A, B):
    # A_i = B_i
    same = 0
    for i in range(N):
        if A[i] == B[i]:
            same += 1
    # A_i = B_j, i != j
    diff = 0
    for i in range(N):
        for j in range(N):
            if i != j and A[i] == B[j]:
                diff += 1
    return same, diff
