def is_triple_double(x, y, z):
    if x == y and y != z:
        return True
    if x == z and x != y:
        return True
    if y == z and y != x:
        return True
    return False
x, y, z = map(int, input().split())
