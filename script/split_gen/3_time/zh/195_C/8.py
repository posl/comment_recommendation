def get_comma_count(n):
    comma_count = 0
    if n >= 1000:
        comma_count += 1
        comma_count += get_comma_count(n // 1000)
    return comma_count
