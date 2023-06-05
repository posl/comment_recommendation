def get_max(a, b, n):
    max = 0
    for x in range(0, n+1):
        temp = (a * x // b) - a * (x // b)
        if temp > max:
            max = temp
    return max
