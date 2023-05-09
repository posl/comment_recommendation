def main():
    N, M = map(int, input().split())
    AC = [False] * N
    WA = [0] * N
    ac_cnt = 0
    wa_cnt = 0
    for i in range(M):
        p, s = input().split()
        p = int(p) - 1
        if AC[p]:
            continue
        if s == 'AC':
            AC[p] = True
            ac_cnt += 1
            wa_cnt += WA[p]
        else:
            WA[p] += 1
    print(ac_cnt, wa_cnt)
