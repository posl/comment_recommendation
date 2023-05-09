def main():
    N, M = map(int, input().split())
    l = [0] * N
    r = [0] * N
    for _ in range(M):
        L, R = map(int, input().split())
        l[L-1] += 1
        r[R-1] += 1
    cnt = 0
    ans = 0
    for i in range(N):
        cnt += l[i]
        if cnt == M:
            ans += 1
        cnt -= r[i]
    print(ans)

if __name__ == '__main__':
    main()