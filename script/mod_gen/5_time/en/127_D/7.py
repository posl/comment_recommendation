def maximum_sum_of_integers(N, M, A, B, C):
    A.sort()
    B.sort(key=lambda x: x[1], reverse=True)
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] < B[j][1]:
            A[i] = B[j][1]
            j += 1
        else:
            break
    return sum(A)

if __name__ == '__main__':
    maximum_sum_of_integers()