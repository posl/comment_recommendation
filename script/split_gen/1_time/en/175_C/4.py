def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x // d >= k:
        print(x - k * d)
    else:
        k = k - x // d
        x = x % d
        if k % 2 == 0:
            print(x)
        else:
            print(abs(x - d))
