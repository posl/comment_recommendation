def main():
    x, a, d, n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
        return
    if a > x:
        if d > 0:
            print(1)
        else:
            print(2)
        return
    if d < 0:
        if a + d * (n - 1) < x:
            print(1)
        else:
            print(2)
        return
    if a + d * (n - 1) < x:
        print(1)
    else:
        print(2)
