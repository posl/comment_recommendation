def main():
    y = int(input())
    while True:
        if y % 4 == 2:
            break
        y += 1
    print(y)

if __name__ == '__main__':
    main()