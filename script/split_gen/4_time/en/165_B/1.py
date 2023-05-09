def main():
    x = int(input())
    balance = 100
    year = 0
    while balance < x:
        year += 1
        balance = int(balance * 1.01)
    print(year)
