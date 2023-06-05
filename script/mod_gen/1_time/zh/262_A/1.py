def main():
    y = int(input())
    while y <= 3000:
        if y % 4 == 2:
            print(y)
            break
        else:
            y = y + 1

if __name__ == '__main__':
    main()