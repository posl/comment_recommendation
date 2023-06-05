def main():
    x = int(input())
    balance = 100
    year = 0
    while True:
        year += 1
        balance = int(balance * 1.01)
        if balance >= x:
            break
    print(year)
