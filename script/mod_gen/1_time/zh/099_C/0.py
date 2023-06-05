def withdraw(money):
    # write your code here
    count = 0
    while money > 0:
        if money >= 729:
            money -= 729
            count += 1
        elif money >= 216:
            money -= 216
            count += 1
        elif money >= 81:
            money -= 81
            count += 1
        elif money >= 36:
            money -= 36
            count += 1
        elif money >= 9:
            money -= 9
            count += 1
        elif money >= 6:
            money -= 6
            count += 1
        elif money >= 1:
            money -= 1
            count += 1
    return count

if __name__ == '__main__':
    withdraw()