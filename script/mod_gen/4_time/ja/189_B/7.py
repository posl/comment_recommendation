def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        v_, p_ = map(int, input().split())
        v.append(v_)
        p.append(p_)
    alc = 0
    for i in range(n):
        alc += v[i] * p[i]
        if alc > x * 100:
            print(i + 1)
            return
    print(-1)

if __name__ == '__main__':
    main()