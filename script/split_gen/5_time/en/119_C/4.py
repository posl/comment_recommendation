def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for i in range(N)]
    ans = 10**9
    for i in range(4**N):
        a = []
        b = []
        c = []
        mp = 0
        for j in range(N):
            if (i >> (2*j)) & 3 == 0:
                a.append(l[j])
            elif (i >> (2*j)) & 3 == 1:
                b.append(l[j])
            elif (i >> (2*j)) & 3 == 2:
                c.append(l[j])
        if len(a) == 0 or len(b) == 0 or len(c) == 0:
            continue
        mp += (len(a) + len(b) + len(c) - 3) * 10
        mp += abs(sum(a) - A)
        mp += abs(sum(b) - B)
        mp += abs(sum(c) - C)
        ans = min(ans, mp)
    print(ans)
