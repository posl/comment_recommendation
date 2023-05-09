def main():
    # Get the number of integers in the sequence.
    n = int(input())
    # Get the sequence of integers.
    a = input().split()
    # Convert the sequence of integers from strings to integers.
    a = [int(x) for x in a]
    # Sort the sequence of integers.
    a.sort()
    # Check if the sequence of integers is a permutation of (1, 2, ..., N).
    if a == list(range(1, n + 1)):
        # If the sequence of integers is a permutation of (1, 2, ..., N), print Yes.
        print("Yes")
    else:
        # If the sequence of integers is not a permutation of (1, 2, ..., N), print No.
        print("No")

if __name__ == '__main__':
    main()