def main():
    n, m = map(int, input().split())
    p = [0] * (n + 1)
    s = [0] * (n + 1)
    for i in range(m):
        p_i, s_i = input().split()
        p_i = int(p_i)
        if s_i == "AC":
            s[p_i] = 1
        else:
            if s[p_i] == 0:
                p[p_i] += 1
    ac = 0
    wa = 0
    for i in range(1, n + 1):
        if s[i] == 1:
            ac += 1
            wa += p[i]
    print(ac, wa)

if __name__ == '__main__':
    main()