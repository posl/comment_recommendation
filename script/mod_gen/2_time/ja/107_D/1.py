def median_of_three(a, b, c):
    if a < b:
        if b < c:
            return b
        elif c < a:
            return a
        else:
            return c
    else:
        if a < c:
            return a
        elif c < b:
            return b
        else:
            return c

if __name__ == '__main__':
    median_of_three()