def rank(x):
    if 0 <= x < 40:
        return 40 - x
    elif 40 <= x < 70:
        return 70 - x
    elif 70 <= x < 90:
        return 90 - x
    elif 90 <= x <= 100:
        return 'expert'
    else:
        return 'error'
x = int(input())
print(rank(x))
