def main():
    y = int(input())
    if y % 4 == 0:
        print(y)
    else:
        print(y + 4 - y % 4)

if __name__ == '__main__':
    main()