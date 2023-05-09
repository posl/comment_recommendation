def main():
    N, M = map(int, input().split())
    switch = [[0 for j in range(N)] for i in range(M)]
    for i in range(M):
        s = list(map(int, input().split()))
        for j in range(s[0]):
            switch[i][s[j+1]-1] = 1
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        f = 1
        for j in range(M):
            if sum([switch[j][k] for k in range(N) if (i >> k) & 1]) % 2 != p[j]:
                f = 0
                break
        ans += f
    print(ans)
main()

if __name__ == '__main__':
    main()