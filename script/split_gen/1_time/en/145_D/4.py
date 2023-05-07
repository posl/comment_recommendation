def main():
    MOD = 10**9 + 7
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    n = (X + Y) // 3
    x = X - n
    y = Y - n
    if x < 0 or y < 0:
        print(0)
        return
    print(comb(n, x, MOD))
