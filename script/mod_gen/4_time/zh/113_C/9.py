def main():
    N, M = map(int, input().split())
    PY = [list(map(int, input().split())) for _ in range(M)]
    PY.sort(key=lambda x: x[1])
    ans = [0] * M
    cnt = [1] * (N + 1)
    for i in range(M):
        p, y = PY[i]
        ans[i] = str(p).zfill(6) + str(cnt[p]).zfill(6)
        cnt[p] += 1
    for i in range(M):
        print(ans[i])

if __name__ == '__main__':
    main()