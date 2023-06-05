def main():
    n, m = map(int, input().split())
    p = [0] * n
    s = [0] * n
    for i in range(m):
        p_i, s_i = input().split()
        p_i = int(p_i)
        if s_i == "AC":
            if p[p_i - 1] != -1:
                s[p_i - 1] = 1
                p[p_i - 1] = -1
        elif s_i == "WA":
            if p[p_i - 1] != -1:
                s[p_i - 1] += 1
    print(sum(s), sum([s[i] for i in range(n) if p[i] == -1]))

if __name__ == '__main__':
    main()