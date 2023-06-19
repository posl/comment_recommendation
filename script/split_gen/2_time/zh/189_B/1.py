def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for _ in range(n):
        v_, p_ = map(int, input().split())
        v.append(v_)
        p.append(p_)
    alc = 0
    for i in range(n):
        alc = alc + v[i] * p[i]
        if alc > x * 100:
            print(i + 1)
            exit()
    print(-1)
