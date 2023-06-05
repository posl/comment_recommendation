def main():
    n, x = map(int, input().split())
    x *= 100
    v, p = [], []
    for _ in range(n):
        v_, p_ = map(int, input().split())
        v.append(v_)
        p.append(p_)
    s = 0
    for i in range(n):
        s += v[i] * p[i]
        if s > x:
            print(i + 1)
            return
    print(-1)

if __name__ == '__main__':
    main()