def interest():
    x = int(input())
    balance = 100
    year = 0
    while balance < x:
        balance = int(balance * 1.01)
        year += 1
    print(year)
interest()

if __name__ == '__main__':
    interest()