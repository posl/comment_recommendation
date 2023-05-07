def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= k * d:
        print(x - k * d)
        return
    else:
        if (k - x // d) % 2 == 0:
            print(abs(x - (x // d) * d))
        else:
            print(abs(x - (x // d + 1) * d))
