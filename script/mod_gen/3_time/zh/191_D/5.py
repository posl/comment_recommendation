def count_points_in_circle(x, y, r):
    import math
    import decimal
    decimal.getcontext().prec = 30
    decimal.getcontext().rounding = decimal.ROUND_HALF_UP
    x = decimal.Decimal(x)
    y = decimal.Decimal(y)
    r = decimal.Decimal(r)
    x_min = math.floor(x - r)
    x_max = math.ceil(x + r)
    y_min = math.floor(y - r)
    y_max = math.ceil(y + r)
    count = 0
    for i in range(x_min, x_max + 1):
        for j in range(y_min, y_max + 1):
            if (x - i)**2 + (y - j)**2 <= r**2:
                count += 1
    return count

if __name__ == '__main__':
    count_points_in_circle()