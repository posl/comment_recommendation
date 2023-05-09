def main():
    n, m = map(int, input().split())
    p = [0] * (n + 1)
    s = [0] * (n + 1)
    ac = [0] * (n + 1)
    wa = [0] * (n + 1)
    for i in range(m):
        p[i], s[i] = input().split()
        p[i] = int(p[i])
        if s[i] == "AC" and ac[p[i]] == 0:
            ac[p[i]] = 1
        elif s[i] == "WA" and ac[p[i]] == 0:
            wa[p[i]] += 1
    ac_count = 0
    wa_count = 0
    for i in range(n + 1):
        if ac[i] == 1:
            ac_count += 1
            wa_count += wa[i]
    print(ac_count, wa_count)
