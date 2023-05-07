def main():
    # Read in the number of integers in the sequence
    N = int(input())
    # Read in the sequence of integers
    A = [int(x) for x in input().split()]
    # Initialize the number of pieces removed
    P = 0
    # Initialize the pieces on each square
    squares = [0, 0, 0, 0]
    # Perform the operations
    for i in range(N):
        # Put a piece on Square 0
        squares[0] += 1
        # Advance every piece on the squares A_i squares ahead
        for j in range(1, 4):
            # If the destination square does not exist, remove the piece
            if j + A[i] >= 4:
                P += squares[j]
                squares[j] = 0
            # Otherwise, move the piece to the destination square
            else:
                squares[j + A[i]] += squares[j]
                squares[j] = 0
    # Print the value of P after all the operations have been performed
    print(P)

if __name__ == '__main__':
    main()