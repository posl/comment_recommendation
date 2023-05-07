def check(x, y, H, W):
    if x < 0 or W <= x or y < 0 or H <= y:
        return False
    return True
