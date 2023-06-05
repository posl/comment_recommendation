def get_min_operation_count(n, q, a, x):
    result = []
    for i in range(q):
        min_count = 0
        for j in range(n):
            min_count += abs(a[j] - x[i])
        result.append(min_count)
    return result

if __name__ == '__main__':
    get_min_operation_count()