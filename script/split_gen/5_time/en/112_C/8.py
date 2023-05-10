def get_distance(x, y, h, cx, cy):
    return max(h - abs(x - cx) - abs(y - cy), 0)
