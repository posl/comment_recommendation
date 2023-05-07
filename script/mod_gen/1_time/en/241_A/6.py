def main():
    # Get input here
    a = list(map(int, input().strip().split()))
    # Calculate result here
    a = a[1:] + [a[0]]
    a = a[1:] + [a[0]]
    a = a[1:] + [a[0]]
    # Print output here
    print(a[0])

if __name__ == '__main__':
    main()