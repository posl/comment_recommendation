def snow_cover(a, b):
    sum = 0
    for i in range(1, b):
        sum += i
        if sum >= a:
            return i
