def exclusive_or(a, b):
    result = 0
    for i in range(a, b + 1):
        result = result ^ i
    return result
