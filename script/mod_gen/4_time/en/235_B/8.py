def main():
    # Get the number of platforms
    N = int(input())
    # Get the height of each platform
    H = list(map(int, input().split()))
    # Initialize the current platform
    current_platform = 0
    # Initialize the next platform
    next_platform = 1
    # Loop through the platforms
    while next_platform < N:
        # If the next platform is higher than the current platform
        if H[next_platform] > H[current_platform]:
            # Move to the next platform
            current_platform = next_platform
        # Move to the next platform
        next_platform += 1
    # Print the height of the final platform
    print(H[current_platform])

if __name__ == '__main__':
    main()