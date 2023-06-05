def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(2**N):
        bit = [0] * N
        for j in range(N):
            if (i >> j) & 1:
                bit[j] = 1
        cnt = [0] * 26
        for j in range(N):
            if bit[j] == 1:
                for k in range(len(S[j])):
                    cnt[ord(S[j][k]) - ord('a')] += 1
        cnt2 = 0
        for j in range(26):
            if cnt[j] > 0:
                cnt2 += 1
        if cnt2 == K:
            ans = max(ans, sum(bit))
    print(ans)

if __name__ == '__main__':
    main()