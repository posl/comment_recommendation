def main():
    year = int(input())
    while year < 2000 or year > 3000:
        year = int(input())
    while year % 4 != 2:
        year += 1
    print(year)
main()
