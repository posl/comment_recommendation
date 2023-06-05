def find_second_player(N, A):
    # A is sorted
    # N is the number of players
    # return the label of the second player
    if N == 1:
        return min(A[0], A[1])
    else:
        # split A into two list
        # A1 and A2
        A1 = A[:2**(N-1)]
        A2 = A[2**(N-1):]
        # find the second player in A1 and A2
        # and then compare them
        second_player1 = find_second_player(N-1, A1)
        second_player2 = find_second_player(N-1, A2)
        second_player = min(second_player1, second_player2)
        return second_player
