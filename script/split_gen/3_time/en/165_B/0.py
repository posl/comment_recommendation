def main():
    X = int(input())
    deposit = 100
    year = 0
    while deposit < X:
        deposit = int(deposit * 1.01)
        year += 1
    print(year)
