def jump(n, x, a, b):
    current = 0
    for i in range(n):
        if (x - current) % a[i] == 0:
            return 'Yes'
        elif (x - current) % b[i] == 0:
            return 'Yes'
        else:
            current += a[i]
    return 'No'
