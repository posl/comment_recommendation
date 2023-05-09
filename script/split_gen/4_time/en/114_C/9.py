def check753(num):
    if num > 1000000000:
        return False
    if num < 100:
        return False
    if num < 1000:
        if num == 375 or num == 537 or num == 573:
            return True
        else:
            return False
    if num < 10000:
        if num == 3573 or num == 3753 or num == 5373 or num == 5733:
            return True
        else:
            return False
    if num < 100000:
        if num == 35753 or num == 35773 or num == 37573 or num == 53753 or num == 53773 or num == 57353:
            return True
        else:
            return False
    if num < 1000000:
        if num == 357373 or num == 537573 or num == 537773 or num == 573373:
            return True
        else:
            return False
    if num < 10000000:
        if num == 3575373 or num == 5375373 or num == 5375733 or num == 5377733 or num == 5735373:
            return True
        else:
            return False
    if num < 100000000:
        if num == 35753773 or num == 53753773 or num == 53757373 or num == 57353773:
            return True
        else:
            return False
    if num < 1000000000:
        if num == 357537773 or num == 537537773 or num == 573537773:
            return True
        else:
            return False
