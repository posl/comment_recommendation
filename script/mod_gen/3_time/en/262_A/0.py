def main():
    y = int(input())
    while True:
        if y % 4 == 2:
            print(y)
            break
        y += 1

if __name__ == '__main__':
    main()