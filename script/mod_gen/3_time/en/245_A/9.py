def main():
    # Read the input
    A, B, C, D = map(int, input().split())
    # Calculate the total minutes past midnight for each person
    time_takahashi = A * 60 + B
    time_aoki = C * 60 + D
    # Compare the times and print the earlier one
    if time_takahashi < time_aoki:
        print("Takahashi")
    else:
        print("Aoki")

if __name__ == '__main__':
    main()