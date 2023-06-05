def getMinCount(money):
    count = 0
    while money > 0:
        if money >= 729:
            money = money - 729
            count = count + 1
        elif money >= 216:
            money = money - 216
            count = count + 1
        elif money >= 81:
            money = money - 81
            count = count + 1
        elif money >= 36:
            money = money - 36
            count = count + 1
        elif money >= 9:
            money = money - 9
            count = count + 1
        elif money >= 6:
            money = money - 6
            count = count + 1
        else:
            money = money - 1
            count = count + 1
    return count
