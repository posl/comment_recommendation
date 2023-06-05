def main():
    X = int(input())
    y = 100
    year = 0
    while y < X:
        y = int(y * 1.01)
        year += 1
    print(year)
