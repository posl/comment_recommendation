def main():
    n, m = map(int, input().split())
    ac = [False] * n
    wa = [0] * n
    ac_count = 0
    wa_count = 0
    for i in range(m):
        p, s = input().split()
        p = int(p) - 1
        if ac[p]:
            continue
        if s == "AC":
            ac[p] = True
            ac_count += 1
            wa_count += wa[p]
        else:
            wa[p] += 1
    print(ac_count, wa_count)
