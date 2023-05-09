def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x - k * d > 0:
        print(x - k * d)
        return
    else:
        if (x - k * d) % (2 * d) == 0:
            print(0)
            return
        else:
            print(abs((x - k * d) % (2 * d) - 2 * d))
            return
