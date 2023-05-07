def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        v_i, p_i = map(int, input().split())
        v.append(v_i)
        p.append(p_i)
    alc = 0
    for i in range(n):
        alc += v[i] * p[i] / 100
        if alc > x:
            print(i + 1)
            return
    print(-1)
