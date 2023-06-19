def dice_sum(a, b, c):
    if a >= 1 and a <= 6 and b >= 1 and b <= 6 and c >= 1 and c <= 6:
        print(7 - a + 7 - b + 7 - c)
    else:
        print("输入的数值不在范围内")
dice_sum(1, 4, 3)
dice_sum(5, 6, 4)
dice_sum(7, 8, 9)
