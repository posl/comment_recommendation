def max_diff(N, A):
    diff = 0
    for i in range(N):
        for j in range(i+1, N):
            if abs(A[i] - A[j]) > diff:
                diff = abs(A[i] - A[j])
    return diff

if __name__ == '__main__':
    max_diff()