def main():
    n, m, x, t, d = map(int, input().split())
    height = t
    for i in range(x, m):
        height += d
    for i in range(m, n):
        height += d
    print(height)
