def get_min_diff(s):
    min_diff = 1000
    for i in range(len(s)-2):
        x = int(s[i:i+3])
        diff = abs(x-753)
        if diff < min_diff:
            min_diff = diff
    return min_diff
