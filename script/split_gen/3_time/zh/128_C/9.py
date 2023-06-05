def main():
    N, M = map(int, input().split())
    k = []
    s = []
    p = []
    for i in range(M):
        k.append(list(map(int, input().split())))
        s.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        ok = True
        for j in range(M):
            cnt = 0
            for l in range(1, k[j][0]+1):
                if (i >> s[j][l-1] - 1) & 1:
                    cnt += 1
            if cnt % 2 != p[j]:
                ok = False
        if ok:
            ans += 1
    print(ans)
