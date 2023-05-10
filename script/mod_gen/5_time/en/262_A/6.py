def main():
    year = int(input())
    while (year % 4) != 2:
        year += 1
    print(year)
    return

if __name__ == '__main__':
    main()