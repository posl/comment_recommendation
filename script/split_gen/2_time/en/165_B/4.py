def main():
    X = int(input())
    year = 0
    balance = 100
    while balance < X:
        year += 1
        balance = int(balance * 1.01)
    print(year)
