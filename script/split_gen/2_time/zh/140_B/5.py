def count_passwords(n):
    if n == 1:
        return 1
    else:
        return count_passwords(n-1) * n
