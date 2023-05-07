def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    X, Y = (X + Y) // 3, (Y - X) // 3
    if X < 0 or Y < 0:
        print(0)
        return
    print(comb(X + Y, X, 10**9 + 7))
