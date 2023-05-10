def dice_sum(a, b):
    if a * 1 <= b <= a * 6:
        return True
    else:
        return False
a, b = map(int, input().split())

if __name__ == '__main__':
    dice_sum()