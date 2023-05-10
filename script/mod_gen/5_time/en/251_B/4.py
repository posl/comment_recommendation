def main():
    # Get input here
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    # Calculate result here
    # Print output here
    print(solve(N, W, A))

if __name__ == '__main__':
    main()