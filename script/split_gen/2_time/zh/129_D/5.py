def is_blocked(x, y, blocked):
    if x < 0 or x >= len(blocked[0]):
        return True
    if y < 0 or y >= len(blocked):
        return True
    return blocked[y][x]
