def main():
    # Read the input
    n = int(input())
    a = list(map(int, input().split()))
    # Compute the product
    product = 1
    for i in range(n):
        product *= a[i]
    # Check if the product is > 10^18
    if product > 10**18:
        print(-1)
    else:
        print(product)

if __name__ == '__main__':
    main()