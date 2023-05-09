def main():
    X = int(input())
    balance = 100
    years = 0
    while (balance < X):
        balance = int(balance * 1.01)
        years += 1
    print(years)
