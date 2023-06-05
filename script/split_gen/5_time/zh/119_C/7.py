def main():
    n, a, b, c = map(int, input().split())
    l = [int(input()) for _ in range(n)]
    ans = 10 ** 9
    for i in range(4 ** n):
        tmp = i
        mp = 0
        la = []
        for j in range(n):
            la.append(tmp % 4)
            tmp //= 4
        if 0 in la[:3]:
            continue
        if 0 not in la[3:]:
            continue
        if 0 in la[3:]:
            mp = 10 * (la.count(0) - 3)
        ta = tb = tc = 0
        for j in range(n):
            if la[j] == 1:
                ta += l[j]
            elif la[j] == 2:
                tb += l[j]
            elif la[j] == 3:
                tc += l[j]
        if ta == 0 or tb == 0 or tc == 0:
            continue
        mp += abs(ta - a) + abs(tb - b) + abs(tc - c)
        ans = min(ans, mp)
    print(ans)
