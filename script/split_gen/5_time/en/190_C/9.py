def count_satisfied_conditions(n, m, a, b, k, c, d):
    max_satisfied_conditions = 0
    for i in range(2 ** k):
        dishes = [0] * n
        for j in range(k):
            if (i >> j) & 1:
                dishes[c[j] - 1] += 1
            else:
                dishes[d[j] - 1] += 1
        satisfied_conditions = 0
        for j in range(m):
            if dishes[a[j] - 1] and dishes[b[j] - 1]:
                satisfied_conditions += 1
        max_satisfied_conditions = max(max_satisfied_conditions, satisfied_conditions)
    return max_satisfied_conditions
