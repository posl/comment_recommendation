def main():
    year = int(input())
    while True:
        if year % 4 == 2:
            print(year)
            break
        year += 1

if __name__ == '__main__':
    main()