def main():
    # Get input here
    A, B, C = map(int, input().strip().split())
    # Calculate result here
    result = 'Yes' if A**2 + B**2 < C**2 else 'No'
    # Print output here
    print(result)

if __name__ == '__main__':
    main()