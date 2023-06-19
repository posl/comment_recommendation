def max_sum(a):
    sum = 0
    minus_count = 0
    min_abs = 10**9+1
    for i in range(len(a)):
        if a[i] < 0:
            minus_count += 1
        sum += abs(a[i])
        min_abs = min(min_abs, abs(a[i]))
    if minus_count % 2 == 0:
        return sum
    else:
        return sum - min_abs*2
