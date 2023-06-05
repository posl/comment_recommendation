def main():
    x = int(input())
    i = 100
    year = 0
    while i < x:
        i = int(i * 1.01)
        year += 1
    print(year)

if __name__ == '__main__':
    main()