def main():
    x = int(input())
    y = 100
    year = 0
    while y < x:
        y = int(y * 1.01)
        year += 1
    print(year)

if __name__ == '__main__':
    main()