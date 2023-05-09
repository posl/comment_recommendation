def get_patty_count(level, layer):
    if level == 0:
        return 1
    elif layer == 1:
        return 0
    elif layer <= (2 ** (level + 1)) - 2:
        return get_patty_count(level - 1, layer - 1)
    elif layer == (2 ** (level + 1)) - 1:
        return (2 ** level) + get_patty_count(level - 1, layer - (2 ** level))
    else:
        return (2 ** level) + get_patty_count(level - 1, (2 ** (level + 1)) - 1 - layer)
