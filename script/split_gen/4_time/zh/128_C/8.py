def main():
    N, M = map(int, input().split())
    k = []
    s = []
    p = []
    for i in range(M):
        ki, *si = map(int, input().split())
        k.append(ki)
        s.append(si)
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1 << N):
        for j in range(M):
            on = 0
            for l in range(k[j]):
                if i & (1 << s[j][l] - 1):
                    on += 1
            if on % 2 != p[j]:
                break
        else:
            ans += 1
    print(ans)
