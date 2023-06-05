def change_money():
    n = int(input())
    print(1000 - n % 1000) if n % 1000 != 0 else print(0)

if __name__ == '__main__':
    change_money()