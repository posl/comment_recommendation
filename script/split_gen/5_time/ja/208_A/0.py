def main():
    dice_count, dice_sum = [int(x) for x in input().split()]
    for i in range(1, dice_count + 1):
        if dice_sum <= i * 6 and dice_sum >= i * 1:
            print("Yes")
            exit()
    print("No")
