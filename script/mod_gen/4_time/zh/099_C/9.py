def getMinCount(num):
    count = 0
    while num > 0:
        if num >= 729:
            count += 1
            num -= 729
        elif num >= 216:
            count += 1
            num -= 216
        elif num >= 81:
            count += 1
            num -= 81
        elif num >= 36:
            count += 1
            num -= 36
        elif num >= 9:
            count += 1
            num -= 9
        elif num >= 6:
            count += 1
            num -= 6
        elif num >= 1:
            count += 1
            num -= 1
    return count

if __name__ == '__main__':
    getMinCount()