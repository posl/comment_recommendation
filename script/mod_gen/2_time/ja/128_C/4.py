def main():
    N, M = map(int, input().split())
    k = [0] * M
    s = [0] * M
    p = [0] * M
    for i in range(M):
        k[i], *s[i] = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for bit in range(2 ** N):
        ok = True
        for i in range(M):
            cnt = 0
            for j in range(k[i]):
                if bit & (1 << (s[i][j] - 1)):
                    cnt += 1
            if cnt % 2 != p[i]:
                ok = False
        if ok:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()