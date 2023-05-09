def main():
    year = int(input())
    while True:
        if year % 4 == 2:
            break
        else:
            year += 1
    print(year)

if __name__ == '__main__':
    main()