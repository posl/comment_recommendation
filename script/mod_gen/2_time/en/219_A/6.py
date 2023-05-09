def main():
    # Get input
    X = int(input())
    # Calculate the minimum number of extra points needed to go up one rank higher
    if X < 40:
        print(40 - X)
    elif X < 70:
        print(70 - X)
    elif X < 90:
        print(90 - X)
    else:
        print("expert")

if __name__ == '__main__':
    main()