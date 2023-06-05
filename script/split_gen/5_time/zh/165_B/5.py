def main():
    X = int(input())
    total = 100
    year = 0
    while total < X:
        total = int(total * 1.01)
        year += 1
    print(year)
