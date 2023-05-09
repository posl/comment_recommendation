def max_diff(list):
    max_diff = 0
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            diff = abs(list[i] - list[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff
