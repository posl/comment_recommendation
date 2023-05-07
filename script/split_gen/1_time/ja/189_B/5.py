def main():
    n, x = map(int, input().split())
    v, p = [], []
    for i in range(n):
        a, b = map(int, input().split())
        v.append(a)
        p.append(b)
    alc = 0
    for i in range(n):
        alc += v[i] * p[i] / 100
        if alc > x:
            print(i + 1)
            return
    print(-1)
    return
