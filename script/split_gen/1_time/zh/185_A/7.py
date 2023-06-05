def get_max_contest_num(a1,a2,a3,a4):
    if a1==a2==a3==a4:
        return 1
    elif (a1==a2 and a3==a4) or (a1==a3 and a2==a4) or (a1==a4 and a2==a3):
        return 2
    elif a1==a2 and a3==a4 and a1==a3 and a2==a4:
        return 3
    else:
        return 0
