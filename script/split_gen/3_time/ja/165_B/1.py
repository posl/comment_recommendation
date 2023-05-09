def main():
    X = int(input())
    money = 100
    year = 0
    while money < X:
        money = money * 101 // 100
        year += 1
    print(year)
