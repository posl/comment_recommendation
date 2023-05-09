def main():
    L, Q = map(int, input().split())
    # Initialize the list of pieces of timber
    pieces = [(0, L)]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            # Cut the piece at Mark x into two
            pieces = cut(pieces, x)
        else:
            # Print the length of the piece with Mark x
            print(length(pieces, x))

if __name__ == '__main__':
    main()