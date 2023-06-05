def main():
    x = int(input())
    total = 100
    year = 0
    while total < x:
        total = int(total * 1.01)
        year += 1
    print(year)

if __name__ == '__main__':
    main()