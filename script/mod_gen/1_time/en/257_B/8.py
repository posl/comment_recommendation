def main():
    # Read input
    # Read N, K, and Q
    N, K, Q = map(int, input().split())
    # Read A_1, A_2, ..., A_K
    A = list(map(int, input().split()))
    # Read L_1, L_2, ..., L_Q
    L = list(map(int, input().split()))
    
    # Initialize the list of squares
    squares = [0] * N
    
    # Place the pieces on the squares
    for i in range(K):
        squares[A[i]-1] = i+1
    
    # Perform the operations
    for i in range(Q):
        # Get the index of the piece
        piece = L[i] - 1
        # Get the index of the square where the piece is
        square = A[piece] - 1
        # If the piece is on its rightmost square, do nothing
        if square == N-1:
            continue
        # If the next square on the right does not contain a piece, move the piece
        if squares[square+1] == 0:
            squares[square] = 0
            squares[square+1] = piece+1
            A[piece] += 1
    
    # Print the indices of the squares on which the pieces are
    print(*[A[i] for i in range(K)])

if __name__ == '__main__':
    main()