def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1 << N):
        if bin(i).count('1') != K:
            continue
        cnt = [0] * 26
        for j in range(N):
            if i >> j & 1:
                for k in S[j]:
                    cnt[ord(k) - ord('a')] += 1
        ans = max(ans, sum(1 for c in cnt if c == K))
    print(ans)
