def main():
    # Get the input
    N, A, B = map(int, input().split())
    # Calculate the minimum total travel expense
    min_expense = min(N * A, B)
    # Print the minimum total travel expense
    print(min_expense)

if __name__ == '__main__':
    main()