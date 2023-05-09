def main():
    N, M = map(int, input().split())
    k = []
    s = []
    p = []
    for i in range(M):
        k_i = list(map(int, input().split()))
        k.append(k_i[0])
        s.append(k_i[1:])
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        ok = True
        for j in range(M):
            cnt = 0
            for l in range(k[j]):
                if (i >> (s[j][l]-1)) & 1:
                    cnt += 1
            if cnt % 2 != p[j]:
                ok = False
        if ok:
            ans += 1
    print(ans)
