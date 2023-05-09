def main():
    a, b, w = map(int, input().split())
    w *= 1000
    n = w//a
    m = w//b
    if n*b <= w <= m*a:
        print(n, m)
    else:
        print("UNSATISFIABLE")
