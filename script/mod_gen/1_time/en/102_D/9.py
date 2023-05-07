def calc_min_diff(arr):
    arr.sort()
    min_diff = 10**9
    for i in range(1, len(arr)-2):
        diff = abs(sum(arr[:i]) - sum(arr[i:]))
        if diff < min_diff:
            min_diff = diff
    return min_diff

if __name__ == '__main__':
    calc_min_diff()