def main():
    # Get the number of coins
    X = int(input())
    # If the number of coins is a multiple of 100, then he has already got the prize
    if X % 100 == 0:
        print(0)
    # Otherwise, he needs to collect 100 - (X % 100) more coins
    else:
        print(100 - (X % 100))

if __name__ == '__main__':
    main()