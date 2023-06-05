def main():
    num = int(input())
    count = 0
    while num != 0:
        if num >= 729:
            num -= 729
            count += 1
        elif num >= 216:
            num -= 216
            count += 1
        elif num >= 81:
            num -= 81
            count += 1
        elif num >= 36:
            num -= 36
            count += 1
        elif num >= 9:
            num -= 9
            count += 1
        elif num >= 6:
            num -= 6
            count += 1
        elif num >= 1:
            num -= 1
            count += 1
    print(count)
