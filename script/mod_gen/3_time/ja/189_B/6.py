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
        alc += v[i] * p[i]
        if alc > x * 100:
            print(i + 1)
            return
    print(-1)
    return

if __name__ == '__main__':
    main()