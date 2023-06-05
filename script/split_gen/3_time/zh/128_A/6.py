def get_max_pie_count(apple_count, piece_count):
    if apple_count == 0 or piece_count == 0:
        return 0
    if apple_count == 1 and piece_count == 1:
        return 1
    if apple_count == 1 and piece_count == 2:
        return 1
    if apple_count == 1 and piece_count == 3:
        return 1
    if apple_count == 2 and piece_count == 1:
        return 2
    if apple_count == 2 and piece_count == 2:
        return 3
    if apple_count == 2 and piece_count == 3:
        return 3
    if apple_count == 3 and piece_count == 1:
        return 3
    if apple_count == 3 and piece_count == 2:
        return 4
    if apple_count == 3 and piece_count == 3:
        return 5
    if apple_count > 3 and piece_count > 3:
        piece_count = piece_count - 3
        return get_max_pie_count(apple_count, piece_count) + 1
    if apple_count > 3 and piece_count <= 3:
        return apple_count + piece_count - 2
