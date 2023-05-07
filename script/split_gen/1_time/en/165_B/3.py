def main():
    X = int(input())
    balance = 100
    years = 0
    while balance < X:
        balance += balance // 100
        years += 1
    print(years)
