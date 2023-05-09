def main():
    X = int(input())
    count = 0
    balance = 100
    while balance < X:
        balance = int(balance * 1.01)
        count += 1
    print(count)
