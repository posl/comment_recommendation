def main():
    # Get input here
    A = list(map(int, input().strip().split()))
    # Calculate result here
    result = min(A[0], A[2], A[3])
    # Print result here
    print(result)
main()
