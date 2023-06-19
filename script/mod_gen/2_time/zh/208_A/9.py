def dice_sum(A, B):
    if A <= 0:
        return False
    if A == 1:
        if B >= 1 and B <= 6:
            return True
        else:
            return False
    else:
        if B >= A and B <= 6 * A:
            return True
        else:
            return False

if __name__ == '__main__':
    dice_sum()