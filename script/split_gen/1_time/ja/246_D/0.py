def main():
    N = int(input())
    X = N
    while True:
        a = 0
        while True:
            b = 0
            while True:
                if X == a**3 + a**2*b + a*b**2 + b**3:
                    print(X)
                    return
                if X < a**3 + a**2*b + a*b**2 + b**3:
                    break
                b += 1
            if X < a**3 + a**2*b + a*b**2 + b**3:
                break
            a += 1
        X += 1
