def getMinCount(money):
    count = 0
    while money > 0:
        if money >= 729:
            money -= 729
        elif money >= 216:
            money -= 216
        elif money >= 81:
            money -= 81
        elif money >= 36:
            money -= 36
        elif money >= 9:
            money -= 9
        elif money >= 6:
            money -= 6
        else:
            money -= 1
        count += 1
    return count

if __name__ == '__main__':
    getMinCount()