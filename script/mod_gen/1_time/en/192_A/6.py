def main():
    X = int(input())
    print(100 - (X % 100))
main()
I used the modulo operator to find the remainder of X divided by 100, and then subtracted that from 100 to find the number of coins needed.

if __name__ == '__main__':
    main()