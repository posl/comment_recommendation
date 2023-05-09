def get_nuts(nuts):
    nuts_taken = 0
    for nut in nuts:
        if nut <= 10:
            continue
        else:
            nuts_taken += nut - 10
    return nuts_taken
