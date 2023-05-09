def is_full_house(a,b,c,d,e):
    if a == b == c:
        if d == e:
            return True
    if a == b:
        if c == d == e:
            return True
    return False

if __name__ == '__main__':
    is_full_house()