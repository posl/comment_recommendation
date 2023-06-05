def dice_sum(A, B):
    if A > 100 or A < 1:
        return False
    if B > 1000 or B < 1:
        return False
    if A == 1 and B < 7:
        return True
    elif A == 1 and B > 6:
        return False
    if B > 6 * A or B < A:
        return False
    if B == 6 * A:
        return True
    if B % A == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    dice_sum()