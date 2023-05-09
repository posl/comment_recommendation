def main():
    Y = int(input())
    if Y % 4 == 2:
        print(Y)
    else:
        print(Y + 2 - Y % 4)

if __name__ == '__main__':
    main()