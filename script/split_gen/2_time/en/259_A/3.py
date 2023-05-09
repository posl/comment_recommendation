def main():
    n, m, x, t, d = map(int, input().split())
    if n == m:
        print(t)
    elif m < x:
        print(t + (x - m) * d)
    else:
        print(t + (n - m) * d)
