def calc_years(x):
    years = 0
    money = 100
    while money < x:
        money = int(money * 1.01)
        years += 1
    return years
x = int(input())
print(calc_years(x))

if __name__ == '__main__':
    calc_years()