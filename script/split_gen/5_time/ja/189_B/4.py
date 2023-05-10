def main():
    n, x = map(int, input().split())
    v = [0] * n
    p = [0] * n
    for i in range(n):
        v[i], p[i] = map(int, input().split())
    a = 0
    for i in range(n):
        a += v[i] * p[i]
        if a > x * 100:
            print(i + 1)
            return
    print(-1)
