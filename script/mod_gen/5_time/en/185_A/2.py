def main():
    # Get input here
    a1, a2, a3, a4 = map(int, input().strip().split())
    # Calculate result here
    result = min(a1, a2, a3, a4)
    # Print output here
    print(result)
main()

if __name__ == '__main__':
    main()