def main():
    # Read input
    x, y = input().split('.')
    # Convert to int
    x = int(x)
    y = int(y)
    # Check if y is in the range
    if y >= 0 and y <= 2:
        print(x, "-", sep="")
    elif y >= 3 and y <= 6:
        print(x)
    else:
        print(x, "+", sep="")

if __name__ == '__main__':
    main()