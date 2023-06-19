def main():
    N = int(input())
    X = N
    while True:
        a = 0
        b = X
        while b > 0:
            a += b % 10
            b //= 10
        if X == N:
            a = 10
        if X == a ** 3 + a ** 2 * a + a * a ** 2 + a ** 3:
            print(X)
            break
        X += 1
