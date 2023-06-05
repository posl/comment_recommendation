def dice_sum(n, s):
    if n == 1 and s <= 6:
        return True
    elif n == 1:
        return False
    else:
        for i in range(1, 7):
            if dice_sum(n-1, s-i):
                return True
        return False

if __name__ == '__main__':
    dice_sum()