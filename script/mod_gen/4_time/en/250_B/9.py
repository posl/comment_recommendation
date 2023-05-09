def main():
    # Get input here
    n, a, b = map(int, input().strip().split())
    # Calculate result here
    result = solve(n, a, b)
    # Output result here
    for line in result:
        print(line)

if __name__ == '__main__':
    main()