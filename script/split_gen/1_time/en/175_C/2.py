def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x < k * d:
        if (k - x // d) % 2 == 0:
            print(x % d)
        else:
            print(abs(x % d - d))
    else:
        print(x - k * d)
