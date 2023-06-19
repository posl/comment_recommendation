def main():
    x = int(input())
    money = 100
    years = 0
    while money < x:
        money = int(money * 1.01)
        years += 1
    print(years)
