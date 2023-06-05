def get_max(a, b, c, d):
    if a*c > a*d:
        if a*c > b*c:
            if a*c > b*d:
                return a*c
            else:
                return b*d
        else:
            if b*c > b*d:
                return b*c
            else:
                return b*d
    else:
        if a*d > b*c:
            if a*d > b*d:
                return a*d
            else:
                return b*d
        else:
            if b*c > b*d:
                return b*c
            else:
                return b*d

if __name__ == '__main__':
    get_max()