def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1 << N):
        tmp = []
        for j in range(N):
            if i & (1 << j):
                tmp.append(S[j])
        tmp = "".join(tmp)
        cnt = 0
        for c in "abcdefghijklmnopqrstuvwxyz":
            cnt += tmp.count(c) == K
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()