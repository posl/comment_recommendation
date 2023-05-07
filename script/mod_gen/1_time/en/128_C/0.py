def main():
    N, M = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(M)]
    P = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        cnt = 0
        for j in range(M):
            tmp = 0
            for k in range(1, S[j][0]+1):
                if (i >> (S[j][k]-1)) & 1:
                    tmp += 1
            if tmp % 2 == P[j]:
                cnt += 1
        if cnt == M:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()