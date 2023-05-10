def water_transfer(a,b,c):
    if a >= b:
        if a >= b + c:
            return 0
        else:
            return b + c - a
    else:
        return c

if __name__ == '__main__':
    water_transfer()