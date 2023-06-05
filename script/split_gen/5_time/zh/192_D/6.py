def get_value(x, base):
    value = 0
    for i in range(len(x)):
        value = value * base + int(x[i])
    return value
