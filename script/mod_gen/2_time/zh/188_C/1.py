def get_second_player(N, A):
    """
    """
    if N == 1:
        return 1 if A[0] > A[1] else 0
    else:
        A1 = A[:2**(N-1)]
        A2 = A[2**(N-1):]
        A1.sort()
        A2.sort()
        if A1[-1] > A2[-1]:
            return get_second_player(N-1, A1)
        else:
            return get_second_player(N-1, A2)

if __name__ == '__main__':
    get_second_player()