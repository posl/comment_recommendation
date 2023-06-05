def get_max_value(vals):
    if len(vals) == 1:
        return vals[0]
    else:
        vals.sort()
        return get_max_value(vals[1:]) + (vals[0] - vals[1]) / 2
