def main():
    y = int(input())
    while True:
        y += 1
        if y % 4 == 2:
            print(y)
            break

if __name__ == '__main__':
    main()