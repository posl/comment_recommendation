def solve():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1 << N):
        if bin(i).count('1') != K:
            continue
        cnt = [0] * 26
        for j in range(N):
            if i >> j & 1:
                for c in S[j]:
                    cnt[ord(c) - ord('a')] += 1
        if max(cnt) == K:
            ans = max(ans, bin(i).count('1'))
    print(ans)
