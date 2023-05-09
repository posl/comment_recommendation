def main():
    x = int(input())
    deposit = 100
    year = 0
    while deposit < x:
        deposit = int(deposit * 1.01)
        year += 1
    print(year)

if __name__ == '__main__':
    main()