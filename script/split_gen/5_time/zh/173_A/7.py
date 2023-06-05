def get_change(money):
    return 1000 - money%1000 if money%1000 != 0 else 0
