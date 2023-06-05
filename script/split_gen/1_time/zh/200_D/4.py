def find_sum_200(A, x, y):
    sum_x = sum([A[i] for i in x])
    sum_y = sum([A[i] for i in y])
    if sum_x % 200 == sum_y % 200 == 0:
        return 0
    else:
        return 1
