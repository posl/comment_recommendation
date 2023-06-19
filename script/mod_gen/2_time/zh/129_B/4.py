def get_min_diff(n, weights):
    min_diff = 1000000
    for i in range(1, n):
        left_sum = sum(weights[:i])
        right_sum = sum(weights[i:])
        diff = abs(left_sum - right_sum)
        if diff < min_diff:
            min_diff = diff
    return min_diff

if __name__ == '__main__':
    get_min_diff()