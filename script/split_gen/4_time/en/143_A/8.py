def main():
    # Take input from user
    A, B = map(int, input().split())
    # Calculate the uncovered part of the window
    uncovered = A - (2 * B)
    # Check if the uncovered part is less than or equal to zero
    if uncovered <= 0:
        # Print zero
        print(0)
    else:
        # Print the uncovered part
        print(uncovered)
