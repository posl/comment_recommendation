def problem165_b():
    x = int(input())
    y = 100
    year = 0
    while y < x:
        y = int(y * 1.01)
        year = year + 1
    print(year)
problem165_b()
