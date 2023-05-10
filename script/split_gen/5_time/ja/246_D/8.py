def main():
    N = int(input())
    X = 0
    while True:
        if X >= N:
            break
        X += 1
        for a in range(1, X + 1):
            for b in range(1, X + 1):
                if X == a ** 3 + a ** 2 * b + a * b ** 2 + b ** 3:
                    print(X)
                    return
