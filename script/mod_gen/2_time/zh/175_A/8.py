def get_max_rainy_days(str):
    max_rainy_days = 0
    rainy_days = 0
    for s in str:
        if s == 'R':
            rainy_days += 1
        else:
            if rainy_days > max_rainy_days:
                max_rainy_days = rainy_days
            rainy_days = 0
    if rainy_days > max_rainy_days:
        max_rainy_days = rainy_days
    return max_rainy_days
str = input()
print(get_max_rainy_days(str))
