def is_triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False

if __name__ == '__main__':
    is_triangle()