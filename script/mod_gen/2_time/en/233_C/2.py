def main():
    N, X = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, 1 << N):
        p = 1
        for j in range(N):
            if i >> j & 1:
                p *= L[j][1 + (i >> j & 1)]
        if X % p == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()