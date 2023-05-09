def count_operations(A, B, C, D):
    cyan = A
    red = 0
    operations = 0
    while cyan > red * D:
        cyan += B
        red += C
        operations += 1
    return operations if cyan <= red * D else -1
