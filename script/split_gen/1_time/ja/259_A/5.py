def main():
    n, m, x, t, d = map(int, input().split())
    if m < x:
        t += d * (m - x)
    print(t)
