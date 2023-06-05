def get_comma_count(n):
    comma_count = 0
    for i in range(1, len(str(n))):
        if i % 3 == 0:
            comma_count += 1
    return comma_count
