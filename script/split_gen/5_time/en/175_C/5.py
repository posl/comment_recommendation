def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= k * d:
        print(x - k * d)
        return
    q = x // d
    if (k - q) % 2 == 0:
        print(x - q * d)
    else:
        print(d - x + q * d)
