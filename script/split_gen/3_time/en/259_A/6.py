def main():
    n, m, x, t, d = [int(i) for i in input().split()]
    print(t + d * (m - x) if m < x else t + d * (n - x))
