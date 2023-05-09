def main():
    X, Y = map(int, input().split())
    MOD = 10**9 + 7
    if (X + Y) % 3 != 0:
        print(0)
        return
    n = (X + Y) // 3
    if X < n or Y < n:
        print(0)
        return
    x = X - n
    y = Y - n
    print(comb(n, x, MOD))
