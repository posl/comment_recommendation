def round_off(x):
    x = float(x)
    if x.is_integer():
        return int(x)
    else:
        return round(x)
