def count_comma(n):
    result = 0
    if n >= 1000:
        result += 1
    if n >= 1000000:
        result += 1
    if n >= 1000000000:
        result += 1
    if n >= 1000000000000:
        result += 1
    if n >= 1000000000000000:
        result += 1
    return result
