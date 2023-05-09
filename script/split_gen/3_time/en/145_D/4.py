def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
    else:
        N = (X + Y) // 3
        if X > N or Y > N:
            print(0)
        else:
            n = N - X
            r = min(X, Y) - n
            print(combination(n + r, r))
