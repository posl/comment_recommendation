def main():
    Y = int(input())
    while Y < 2000 or Y > 3000:
        Y = int(input())
    print(Y + 2 - (Y % 4))

if __name__ == '__main__':
    main()