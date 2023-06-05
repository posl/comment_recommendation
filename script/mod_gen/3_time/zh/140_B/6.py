def get_sum(N, A, B, C):
    sum = 0
    for i in range(N):
        sum += B[A[i]-1]
        if i < N-1 and A[i+1]-A[i] == 1:
            sum += C[A[i]-1]
    return sum

if __name__ == '__main__':
    get_sum()