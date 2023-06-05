def get_min_diff(s):
    min_diff = 753 - int(s[:3])
    for i in range(len(s)-2):
        temp = abs(int(s[i:i+3]) - 753)
        if temp < min_diff:
            min_diff = temp
    return min_diff
