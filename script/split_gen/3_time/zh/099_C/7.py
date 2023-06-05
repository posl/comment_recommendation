def cal_min_operations(n):
    if n <= 0:
        return 0
    else:
        min_operations = n
        for i in range(1, n):
            operations = 1 + cal_min_operations(n - i ** 2)
            if operations < min_operations:
                min_operations = operations
        return min_operations
