def is_full_house(a, b, c, d, e):
    if a == b and b == c and d == e:
        return True
    if a == b and c == d and d == e:
        return True
    return False
a, b, c, d, e = map(int, input().split())

if __name__ == '__main__':
    is_full_house()