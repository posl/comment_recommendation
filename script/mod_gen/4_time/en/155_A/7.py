def poor_triple(a, b, c):
    if a == b and b != c:
        return True
    if b == c and c != a:
        return True
    if c == a and a != b:
        return True
    return False

if __name__ == '__main__':
    poor_triple()