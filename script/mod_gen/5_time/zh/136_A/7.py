def pour_water(a,b,c):
    if a >= b+c:
        return 0
    elif a >= b:
        return c-(a-b)
    else:
        return c-(a-b)

if __name__ == '__main__':
    pour_water()