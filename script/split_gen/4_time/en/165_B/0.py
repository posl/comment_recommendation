def main():
    x = int(input())
    balance = 100
    years = 0
    while balance < x:
        balance = int(balance * 1.01)
        years += 1
    print(years)
