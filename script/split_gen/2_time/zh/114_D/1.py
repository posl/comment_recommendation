def count_75(n):
    count = 0
    for i in range(1, n + 1):
        j = i
        while j % 5 == 0:
            j //= 5
        while j % 3 == 0:
            j //= 3
        while j % 2 == 0:
            j //= 2
        if j == 1:
            count += 1
    return count
