def main():
    # Read data from stdin
    A = list(map(int, input().split()))
    # Sort the list
    A.sort()
    # Check if the difference between the first and second element is equal to the difference between the second and third element.
    if A[2] - A[1] == A[1] - A[0]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()