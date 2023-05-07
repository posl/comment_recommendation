def main():
    x, k, d = [int(i) for i in input().split()]
    x = abs(x)
    if x // d >= k:
        print(x - k * d)
    else:
        if (k - x // d) % 2 == 0:
            print(x % d)
        else:
            print(abs(x % d - d))
