def main():
    y = int(input())
    while y < 2000 or y > 3000:
        y = int(input())
    while y % 4 != 2:
        y += 1
    print(y)

if __name__ == '__main__':
    main()