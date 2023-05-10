def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for i in range(N)]
    ans = 10**10
    for i in range(4**N):
        mp = 0
        a = []
        b = []
        c = []
        for j in range(N):
            if (i >> (2*j)) & 1 == 1:
                a.append(l[j])
            elif (i >> (2*j + 1)) & 1 == 1:
                b.append(l[j])
            else:
                c.append(l[j])
        if len(a) == 0 or len(b) == 0 or len(c) == 0:
            continue
        mp += (len(a) - 1 + len(b) - 1 + len(c) - 1) * 10
        mp += abs(sum(a) - A)
        mp += abs(sum(b) - B)
        mp += abs(sum(c) - C)
        ans = min(ans, mp)
    print(ans)
