def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        vi, pi = map(int, input().split())
        v.append(vi)
        p.append(pi)
    total = 0
    for i in range(n):
        total += v[i] * p[i]
        if total > x * 100:
            print(i + 1)
            return
    print(-1)
