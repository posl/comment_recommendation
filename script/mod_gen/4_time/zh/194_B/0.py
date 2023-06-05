def get_min_time(N, A, B):
    min_time = float('inf')
    for i in range(N):
        for j in range(N):
            if i == j:
                min_time = min(min_time, A[i]+B[j])
            else:
                min_time = min(min_time, max(A[i], B[j]))
    return min_time

if __name__ == '__main__':
    get_min_time()