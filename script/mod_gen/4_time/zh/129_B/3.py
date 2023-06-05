def get_min_abs_diff(n, weights):
    min_abs_diff = 100000
    for i in range(1, n):
        left = weights[:i]
        right = weights[i:]
        left_sum = sum(left)
        right_sum = sum(right)
        abs_diff = abs(left_sum - right_sum)
        if abs_diff < min_abs_diff:
            min_abs_diff = abs_diff
    return min_abs_diff

if __name__ == '__main__':
    get_min_abs_diff()