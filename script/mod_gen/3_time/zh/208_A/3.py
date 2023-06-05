def dice_sum(a,b):
    for i in range(1,7):
        for j in range(1,7):
            if a*i+j == b:
                return True
    return False

if __name__ == '__main__':
    dice_sum()