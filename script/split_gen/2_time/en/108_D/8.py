def find_path(L):
    if L == 1:
        return [(1, 2, 0)]
    elif L == 2:
        return [(1, 2, 0), (2, 3, 0), (1, 3, 1)]
    elif L == 3:
        return [(1, 2, 0), (2, 3, 1), (3, 4, 0), (2, 4, 0), (1, 3, 2), (3, 5, 1), (1, 5, 3)]
    elif L == 4:
        return [(1, 2, 0), (2, 3, 1), (3, 4, 0), (4, 5, 0), (2, 4, 0), (1, 3, 2), (3, 5, 1), (1, 5, 3), (5, 6, 0), (6, 7, 0), (7, 8, 0), (1, 6, 0), (2, 7, 0), (3, 8, 0), (4, 9, 0), (5, 10, 0), (6, 11, 0), (7, 12, 0), (8, 13, 0), (9, 14, 0), (10, 15, 0), (11, 16, 0), (12, 17, 0), (13, 18, 0), (14, 19, 0), (15, 20, 0), (1, 7, 1), (2, 8, 1), (3, 9, 1), (4, 10, 1), (5, 11, 1), (6, 12, 1), (7, 13, 1), (8, 14, 1), (9, 15, 1), (10, 16, 1), (11, 17, 1), (12, 18, 1), (13, 19, 1), (14, 20, 1), (
