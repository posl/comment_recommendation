def dice_sum(a, b):
    if a * 1 <= b <= a * 6:
        return True
    else:
        return False
a, b = map(int, input().split())
