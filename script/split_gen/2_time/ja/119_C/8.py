def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    ans = 100000000
    for i in range(4**N):
        a, b, c = 0, 0, 0
        a_mp, b_mp, c_mp = 0, 0, 0
        for j in range(N):
            if (i >> (j*2)) & 3 == 0:
                a += l[j]
                a_mp += 10 * (l[j]-1)
            elif (i >> (j*2)) & 3 == 1:
                b += l[j]
                b_mp += 10 * (l[j]-1)
            elif (i >> (j*2)) & 3 == 2:
                c += l[j]
                c_mp += 10 * (l[j]-1)
        if a != 0 and b != 0 and c != 0:
            a_mp += abs(a-A)
            b_mp += abs(b-B)
            c_mp += abs(c-C)
            ans = min(ans, a_mp+b_mp+c_mp-30)
    print(ans)
