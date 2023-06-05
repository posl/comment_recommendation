def min_sadness(N, A):
    b = 0
    sadness = 0
    for i in range(N):
        sadness += abs(A[i] - (b + i + 1))
    return sadness

if __name__ == '__main__':
    min_sadness()