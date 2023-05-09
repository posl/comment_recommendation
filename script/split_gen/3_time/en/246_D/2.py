def main():
    N = int(input())
    for X in range(N, 10**18+1):
        for a in range(0, 10000):
            for b in range(0, 10000):
                if X == a**3 + a**2*b + a*b**2 + b**3:
                    print(X)
                    return
