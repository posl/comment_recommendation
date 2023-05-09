def main():
    # Read the numbers from the standard input
    X, Y, Z = map(int, input().split())
    # Swap the contents of the boxes A and B
    X, Y = Y, X
    # Swap the contents of the boxes A and C
    X, Z = Z, X
    # Print the integers contained in the boxes A, B, and C, in this order, with space in between.
    print(X, Y, Z)
