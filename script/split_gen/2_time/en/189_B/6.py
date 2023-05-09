def main():
    n, x = map(int, input().split())
    v, p = [], []
    for i in range(n):
        v_i, p_i = map(int, input().split())
        v.append(v_i)
        p.append(p_i)
    for i in range(n):
        x -= v[i] * p[i] / 100
        if x < 0:
            print(i + 1)
            return
    print(-1)
