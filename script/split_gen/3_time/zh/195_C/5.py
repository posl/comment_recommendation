def count_comma(n):
    if n < 1000:
        return 0
    else:
        return count_comma(n // 1000) + 1
