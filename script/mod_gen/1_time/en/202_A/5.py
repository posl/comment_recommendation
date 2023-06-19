def dice_sum():
    dice = list(map(int, input().split()))
    print(21 - sum(dice))
dice_sum()
