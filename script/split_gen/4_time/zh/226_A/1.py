def round(x):
    if x - int(x) < 0.5:
        return int(x)
    else:
        return int(x) + 1
