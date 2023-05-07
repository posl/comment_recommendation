def main():
    N = int(input())
    X = N
    while True:
        a, b = 0, 0
        while a**3 + a**2*b + a*b**2 + b**3 < X:
            b += 1
        while a**3 + a**2*b + a*b**2 + b**3 < X:
            a += 1
        if a**3 + a**2*b + a*b**2 + b**3 == X:
            print(X)
            break
        X += 1
