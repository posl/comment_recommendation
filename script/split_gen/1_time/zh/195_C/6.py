def count_comma(n):
    if n < 1000:
        return 0
    else:
        count = 0
        while n > 1000:
            count += 1
            n = n / 1000
        return count
