def calc_ferris_wheel_cost(age, cost):
    if age >= 13:
        return cost
    elif age >= 6:
        return cost / 2
    else:
        return 0
