def get_nuts(nuts):
    sum = 0
    for nut in nuts:
        if nut > 10:
            sum += nut - 10
    return sum
