def main():
    x, y = map(int, input().split())
    if (x + y) % 3 != 0 or x < y:
        print(0)
        return
    n = (x + y) // 3
    k = x - n
    print(comb(n, k))
