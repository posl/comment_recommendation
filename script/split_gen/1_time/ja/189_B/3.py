def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        vi, pi = map(int, input().split())
        v.append(vi)
        p.append(pi)
    alc = 0
    for i in range(n):
        alc += v[i] * p[i] / 100
        if alc > x:
            print(i + 1)
            return
    print(-1)
