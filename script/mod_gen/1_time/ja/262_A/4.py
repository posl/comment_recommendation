def main():
    Y = int(input())
    while Y % 4 != 2:
        Y += 1
    print(Y)

if __name__ == '__main__':
    main()