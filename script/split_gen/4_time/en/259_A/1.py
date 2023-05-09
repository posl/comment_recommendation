def main():
    n, m, x, t, d = map(int, input().split())
    for i in range(m, n):
        t += d
        if i == x - 1:
            d = 0
    print(t)
