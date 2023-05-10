def main():
    # Read from stdin
    n = int(input())
    # Initialize variables
    mountains = {}
    for i in range(n):
        # Read from stdin
        name, height = input().split()
        # Add to dictionary
        mountains[name] = int(height)
    # Find the second highest mountain
    second_highest = sorted(mountains.items(), key=lambda x: x[1], reverse=True)[1][0]
    # Print to stdout
    print(second_highest)

if __name__ == '__main__':
    main()