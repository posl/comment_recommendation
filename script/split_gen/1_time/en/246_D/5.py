def main():
    N = int(input())
    if N == 0:
        print(0)
        exit()
    X = N
    while True:
        for a in range(1000):
            for b in range(1000):
                if X == a**3 + a**2*b + a*b**2 + b**3:
                    print(X)
                    exit()
        X += 1
