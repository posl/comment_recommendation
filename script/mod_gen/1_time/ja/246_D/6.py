def main():
    N = int(input())
    # N = 0
    # N = 999999999989449206
    X = N
    X1 = X
    while True:
        X2 = X1
        for a in range(0, 10**5):
            for b in range(0, 10**5):
                if X1 == a**3 + a**2*b + a*b**2 + b**3:
                    print(X1)
                    return
                if X1 < a**3 + a**2*b + a*b**2 + b**3:
                    break
        X1 += 1
        if X1 > 10**18:
            print(-1)
            return
        if X1 == X2:
            print(-1)
            return

if __name__ == '__main__':
    main()