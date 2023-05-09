def main():
    year = int(input())
    if year % 100 == 0:
        print(year // 100)
    else:
        print(year // 100 + 1)

if __name__ == '__main__':
    main()