def throw_dice(n, m):
    if (n < 1 or m < 1):
        return False
    if (n == 1):
        if (m >= 1 and m <= 6):
            return True
        else:
            return False
    else:
        return throw_dice(n - 1, m - 1) or throw_dice(n - 1, m - 2) or throw_dice(n - 1, m - 3) or throw_dice(n - 1, m - 4) or throw_dice(n - 1, m - 5) or throw_dice(n - 1, m - 6)
print(throw_dice(100, 600))
print(throw_dice(2, 13))
print(throw_dice(2, 11))
