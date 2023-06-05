def check_if_full_house(a,b,c,d,e):
    if a == b and b == c and d == e:
        return True
    elif a == b and c == d and d == e:
        return True
    else:
        return False

if __name__ == '__main__':
    check_if_full_house()