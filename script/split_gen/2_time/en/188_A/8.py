def can_turn_tables(x, y):
    if x < y:
        return "Yes" if y - x >= 3 else "No"
    else:
        return "Yes" if x - y >= 3 else "No"
