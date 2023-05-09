def sum_of_integers(N, A, B):
    sum = 0
    for i in range(1, N+1):
        if not (i % A == 0 or i % B == 0):
            sum += i
    return sum
