def survive(N, K, Q, A):
    score = [K] * N
    for i in range(Q):
        score[A[i]-1] -= 1
    for i in range(N):
        if score[i] > 0:
            print("Yes")
        else:
            print("No")
