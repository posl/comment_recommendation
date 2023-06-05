def max_sum(N, B):
    A = [0] * N
    A[0] = B[0]
    for i in range(N-2):
        A[i+1] = max(B[i], B[i+1])
    A[N-1] = B[N-2]
    return sum(A)

if __name__ == '__main__':
    max_sum()