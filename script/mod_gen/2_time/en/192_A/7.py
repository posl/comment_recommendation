def main():
    # Read the input
    X = int(input())
    # Find the number of coins needed to get the next prize
    coins_needed = 100 - (X % 100)
    # Print the result
    print(coins_needed)

if __name__ == '__main__':
    main()