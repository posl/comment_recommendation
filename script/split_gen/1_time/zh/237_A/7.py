def is_in_range(n):
    if -2**31 <= n and n <= 2**31 - 1:
        return True
    else:
        return False
