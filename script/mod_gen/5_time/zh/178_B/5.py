def max_product(a,b,c,d):
    if a*c>=a*d and a*c>=b*c and a*c>=b*d:
        return a*c
    elif a*d>=a*c and a*d>=b*c and a*d>=b*d:
        return a*d
    elif b*c>=a*c and b*c>=a*d and b*c>=b*d:
        return b*c
    else:
        return b*d

if __name__ == '__main__':
    max_product()