def get_nuts_number(nuts):
    nuts_number = 0
    for nut in nuts:
        if nut > 10:
            nuts_number += nut - 10
    return nuts_number
