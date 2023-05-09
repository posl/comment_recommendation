def min_time(N, A, B):
    min_time = 10**10
    for i in range(N):
        for j in range(N):
            if i == j:
                time = A[i] + B[j]
            else:
                time = max(A[i], B[j])
            if time < min_time:
                min_time = time
    return min_time

if __name__ == '__main__':
    min_time()