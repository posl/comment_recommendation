def main():
    # Read the number of operations
    n = int(input())
    # Read the number of squares to advance
    squares = [int(x) for x in input().split()]
    # Keep track of the number of pieces removed
    pieces_removed = 0
    # Keep track of the number of pieces on each square
    pieces_on_square = [0, 0, 0, 0]
    # Put a piece on square 0
    pieces_on_square[0] = 1
    # For each number of squares to advance
    for num_squares in squares:
        # For each square
        for i in range(4):
            # If there is a piece on the square
            if pieces_on_square[i] > 0:
                # If the destination square exists
                if i + num_squares < 4:
                    # Move the piece to the destination square
                    pieces_on_square[i + num_squares] += 1
                # Otherwise, the destination square does not exist
                else:
                    # Remove the piece
                    pieces_removed += 1
        # Put a piece on square 0
        pieces_on_square[0] = 1
    # Print the number of pieces removed
    print(pieces_removed)
