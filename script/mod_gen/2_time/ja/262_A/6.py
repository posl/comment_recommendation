def main():
    year = int(input())
    while True:
        year = year + 1
        if year % 4 == 2:
            break
    print(year)

if __name__ == '__main__':
    main()