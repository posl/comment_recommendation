def triangle(a, b, c):
    if a < b + c and b < c + a and c < a + b:
        return 1
    else:
        return 0

if __name__ == '__main__':
    triangle()