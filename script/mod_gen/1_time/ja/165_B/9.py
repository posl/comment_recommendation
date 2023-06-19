def calc_years(x):
    y = 100
    years = 0
    while y < x:
        y = (y * 101) // 100
        years += 1
    return years
x = int(input())
print(calc_years(x))
