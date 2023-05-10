def main():
    year = int(input())
    while year % 4 != 2:
        year += 1
    print(year)
