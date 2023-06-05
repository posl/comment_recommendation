def min_move(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        count = 0
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = n - 1
            count += 1
        return count
