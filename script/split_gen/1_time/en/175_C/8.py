def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    m = x // d
    if m == 0:
        print(x - k * d)
        return
    if m >= k:
        print(x - k * d)
        return
    k -= m
    x -= m * d
    if k % 2 == 0:
        print(x)
    else:
        print(abs(x - d))
