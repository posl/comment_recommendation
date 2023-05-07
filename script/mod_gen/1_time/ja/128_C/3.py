def main():
    N, M = map(int, input().split())
    S = [list(map(int, input().split())) for i in range(M)]
    P = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        bit = [0]*N
        for j in range(N):
            if (i >> j) & 1:
                bit[j] = 1
        for j in range(M):
            cnt = 0
            for s in S[j][1:]:
                if bit[s-1] == 1:
                    cnt += 1
            if cnt % 2 != P[j]:
                break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()