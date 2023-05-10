def main():
    n, m, x, t, d = map(int, input().split())
    age = 0
    height = t
    for i in range(1, x):
        age += 1
        height += d
    for i in range(x, m):
        age += 1
    for i in range(m, n):
        age += 1
        height += d
    print(height)
