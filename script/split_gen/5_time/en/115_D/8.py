def calc_patties(n, x):
    if n == 0:
        return 1
    elif x == 1:
        return 0
    elif x < 2 + (2 ** n - 1):
        return calc_patties(n - 1, x - 1)
    elif x == 2 + (2 ** n - 1):
        return 1 + (2 ** n - 1)
    elif x < 3 + (2 ** n - 1) * 2:
        return 1 + (2 ** n - 1) + calc_patties(n - 1, x - (2 + (2 ** n - 1)))
    elif x == 3 + (2 ** n - 1) * 2:
        return 1 + (2 ** n - 1) * 2
    else:
        return 1 + (2 ** n - 1) * 2 + calc_patties(n - 1, x - (3 + (2 ** n - 1) * 2))
