def get_count(N, A):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if (A[i]+A[j])%2 == 0:
                count += 1
    return count
