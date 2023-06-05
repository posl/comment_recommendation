def problems130_d(N, K, A):
    count = 0
    start = 0
    end = 0
    sum = A[0]
    while start < N and end < N:
        if sum < K:
            end += 1
            if end < N:
                sum += A[end]
        else:
            count += N - end
            sum -= A[start]
            start += 1
    return count
