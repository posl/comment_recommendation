def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        v_i, p_i = map(int, input().split())
        v.append(v_i)
        p.append(p_i)
    sum = 0
    for i in range(n):
        sum += v[i] * p[i] / 100
        if sum > x:
            print(i + 1)
            return
    print(-1)

if __name__ == '__main__':
    main()