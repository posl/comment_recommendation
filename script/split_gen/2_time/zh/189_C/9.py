def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        v_temp, p_temp = map(int, input().split())
        v.append(v_temp)
        p.append(p_temp)
    sum = 0
    for i in range(n):
        sum += v[i] * p[i]
        if sum > x * 100:
            print(i + 1)
            return
    print(-1)
    return
main()
