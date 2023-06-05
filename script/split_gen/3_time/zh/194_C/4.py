def sum_of_square_difference(A):
    return sum([sum([(A[i] - A[j]) ** 2 for j in range(i)]) for i in range(1, len(A))])
