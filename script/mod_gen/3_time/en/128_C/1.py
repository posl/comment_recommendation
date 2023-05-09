def main():
    N, M = map(int, input().split())
    k = [0] * M
    s = [[0] * N for _ in range(M)]
    p = [0] * M
    for i in range(M):
        s[i] = list(map(int, input().split()))
        k[i] = s[i][0]
        s[i].pop(0)
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        cnt = 0
        for j in range(M):
            c = 0
            for l in range(k[j]):
                if (i >> (s[j][l] - 1)) & 1:
                    c += 1
            if c % 2 == p[j]:
                cnt += 1
        if cnt == M:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()