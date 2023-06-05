def throw_dice(num, target):
    if num == 1:
        if 1 <= target <= 6:
            return True
        else:
            return False
    else:
        for i in range(1, 7):
            if throw_dice(num-1, target - i):
                return True
        return False

if __name__ == '__main__':
    throw_dice()