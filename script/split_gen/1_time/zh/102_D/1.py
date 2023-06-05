def get_max_min_diff(a):
    n = len(a)
    max_diff = 0
    for i in range(1, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                max_diff = max(max_diff, abs(sum(a[:i]) - sum(a[i:j]) - sum(a[j:k]) + sum(a[k:])))
    return max_diff
