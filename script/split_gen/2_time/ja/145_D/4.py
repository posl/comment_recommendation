def main():
    x, y = map(int, input().split())
    mod = 10**9+7
    if (x+y) % 3 != 0:
        print(0)
        return
    n = (x+y) // 3
    if x < n or y < n:
        print(0)
        return
    x -= n
    y -= n
    print(comb(n, x, mod))
