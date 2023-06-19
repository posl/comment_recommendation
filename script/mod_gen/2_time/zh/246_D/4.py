def check(x):
    a = 0
    b = x
    while a <= b:
        if a**3 + a**2*b + a*b**2 + b**3 == x:
            return True
        elif a**3 + a**2*b + a*b**2 + b**3 < x:
            a += 1
        else:
            b -= 1
    return False

if __name__ == '__main__':
    check()