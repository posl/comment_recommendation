def max_monster(N, A, B):
    count = 0
    for i in range(N):
        if A[i] >= B[i]:
            count += B[i]
        else:
            count += A[i]
            B[i] -= A[i]
            if A[i + 1] >= B[i]:
                count += B[i]
                A[i + 1] -= B[i]
            else:
                count += A[i + 1]
                A[i + 1] = 0
    return count

if __name__ == '__main__':
    max_monster()