def solution(n, a):
    s = sum(a)
    min_diff = 1e9
    for i in range(1, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                p = sum(a[:i])
                q = sum(a[i:j])
                r = sum(a[j:k])
                s = sum(a[k:])
                min_diff = min(min_diff, max(p, q, r, s) - min(p, q, r, s))
    return min_diff
