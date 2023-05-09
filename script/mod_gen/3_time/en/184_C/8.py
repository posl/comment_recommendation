def get_move_count(r1, c1, r2, c2):
    # If the distance between two points is 3 or less, then the minimum number of moves is 1.
    if abs(r1 - r2) + abs(c1 - c2) <= 3:
        return 1
    # If the distance between two points is 6 or less, then the minimum number of moves is 2.
    if abs(r1 - r2) + abs(c1 - c2) <= 6:
        return 2
    # If the distance between two points is 7 or less, then the minimum number of moves is 3.
    if abs(r1 - r2) + abs(c1 - c2) <= 7:
        return 3
    # If the distance between two points is 8 or less, then the minimum number of moves is 4.
    if abs(r1 - r2) + abs(c1 - c2) <= 8:
        return 4
    # If the distance between two points is 9 or less, then the minimum number of moves is 5.
    if abs(r1 - r2) + abs(c1 - c2) <= 9:
        return 5
    # If the distance between two points is 10 or less, then the minimum number of moves is 6.
    if abs(r1 - r2) + abs(c1 - c2) <= 10:
        return 6
    # If the distance between two points is 11 or less, then the minimum number of moves is 7.
    if abs(r1 - r2) + abs(c1 - c2) <= 11:
        return 7
    # If the distance between two points is 12 or less, then the minimum number of moves is 8.
    if abs(r1 - r2) + abs(c1 - c2) <= 12:
        return 8
    # If the distance between two points is 13 or less, then the minimum number of moves is 9.
    if abs(r1 - r2) + abs(c1 - c2) <= 13:
        return 9
    # If the distance between two points is 14 or less, then the minimum number of moves is 10.
    if abs(r1 - r2) + abs

if __name__ == '__main__':
    get_move_count()