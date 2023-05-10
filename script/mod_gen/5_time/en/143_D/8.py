def triangle(a,b,c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False

if __name__ == '__main__':
    triangle()