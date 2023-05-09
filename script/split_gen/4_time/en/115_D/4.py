def main():
    n, x = map(int, input().split())
    patty = 0
    bun = 1
    for i in range(n):
        patty = 2 * patty + 1
        bun = 2 * bun + 3
    while x > 0:
        if x == bun:
            x -= bun
            patty += 1
        elif x > bun // 2:
            x -= bun // 2 + 1
            patty += patty + 1
        else:
            x -= 1
        n -= 1
        patty //= 2
        bun = 2 * bun + 3
    print(patty)
