def main():
    #n, m = map(int, input().split())
    #p = [0] * m
    #s = [0] * m
    #for i in range(m):
    #    p[i], s[i] = input().split()
    #    p[i] = int(p[i])
    #    s[i] = str(s[i])
    n, m = 6, 0
    p = [0] * m
    s = [0] * m
    p = [1, 1, 2, 2, 2]
    s = ["WA", "AC", "WA", "AC", "WA"]
    print(p)
    print(s)
    ac = [0] * n
    wa = [0] * n
    for i in range(m):
        if s[i] == "AC":
            ac[p[i] - 1] = 1
        else:
            if ac[p[i] - 1] == 0:
                wa[p[i] - 1] += 1
    print(ac)
    print(wa)
    ac_count = 0
    wa_count = 0
    for i in range(n):
        if ac[i] == 1:
            ac_count += 1
            wa_count += wa[i]
    print(ac_count, wa_count)
