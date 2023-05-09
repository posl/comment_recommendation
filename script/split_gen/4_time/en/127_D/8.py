def maximum_sum_of_cards(N, M, A, B, C):
    A.sort()
    operations = sorted(zip(B, C), key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in operations:
        if A[i] < c:
            for j in range(b):
                if A[i] >= c:
                    break
                A[i] = c
                i += 1
    return sum(A)
