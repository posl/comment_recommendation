def main():
    # Read the number of dimensions
    n = int(input())
    # Read the first vector
    a = list(map(int, input().split()))
    # Read the second vector
    b = list(map(int, input().split()))
    # Compute the inner product
    ip = sum([a[i] * b[i] for i in range(n)])
    # Print the result
    print('Yes' if ip == 0 else 'No')

if __name__ == '__main__':
    main()