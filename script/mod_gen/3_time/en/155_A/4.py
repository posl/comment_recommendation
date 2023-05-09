def poor(a,b,c):
    if a == b and a != c:
        return True
    if a == c and a != b:
        return True
    if b == c and b != a:
        return True
    return False

if __name__ == '__main__':
    poor()