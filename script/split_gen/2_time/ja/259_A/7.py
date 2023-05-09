def calc_height(n, m, x, t, d):
    if m <= x:
        result = t + (m-1)*d
        for i in range(m, x):
            result += d
        return result
    else:
        result = t + (x-1)*d
        for i in range(x, m):
            result -= d
        return result
