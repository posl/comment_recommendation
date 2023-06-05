def solution(h, n, a):
    a.sort()
    for i in range(n):
        h -= a[i]
        if h <= 0:
            return "Yes"
    return "No"
