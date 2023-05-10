def pow(a, b):
    if a >= 0:
        return a**b
    else:
        if b % 2 == 0:
            return (-a)**b
        else:
            return -((-a)**b)
A, B, C = map(int, input().split())

if __name__ == '__main__':
    pow()