def main():
    # Get input
    N, R = map(int, input().split())
    # Calculate Inner Rating
    IR = R + 100 * (10 - N)
    # Print Inner Rating
    print(IR)

if __name__ == '__main__':
    main()