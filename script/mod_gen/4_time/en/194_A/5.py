def ice_cream_type(milk_solids, milk_fat):
    if milk_solids >= 15 and milk_fat >= 8:
        return 1
    elif milk_solids >= 10 and milk_fat >= 3:
        return 2
    elif milk_solids >= 3:
        return 3
    else:
        return 4

if __name__ == '__main__':
    ice_cream_type()