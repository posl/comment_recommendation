def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        v_, p_ = map(int, input().split())
        v.append(v_)
        p.append(p_)
    vol = 0
    for i in range(n):
        vol += v[i] * p[i] / 100
        if vol > x:
            print(i + 1)
            return
    print(-1)
