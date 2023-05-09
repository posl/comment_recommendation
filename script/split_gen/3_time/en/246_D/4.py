def main():
    N = int(input())
    X = N
    while True:
        a = 0
        b = 0
        while True:
            if X < a**3 + a**2*b + a*b**2 + b**3:
                break
            if X == a**3 + a**2*b + a*b**2 + b**3:
                print(X)
                return
            b += 1
        a += 1
        X += 1
