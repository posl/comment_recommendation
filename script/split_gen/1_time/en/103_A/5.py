def main():
    # Get input here
    A = list(map(int, input().strip().split()))
    # Calculate result here
    A.sort()
    print(A[2] - A[0])
    # Print result here
main()
