def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if k <= x // d:
        print(x - k * d)
    else:
        k -= x // d
        x %= d
        if k % 2 == 0:
            print(x)
        else:
            print(d - x)
