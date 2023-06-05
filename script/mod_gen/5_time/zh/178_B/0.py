def max_product(a,b,c,d):
    if a*c > a*d:
        if a*c > b*c:
            return a*c
        else:
            return b*c
    else:
        if a*d > b*d:
            return a*d
        else:
            return b*d

if __name__ == '__main__':
    max_product()