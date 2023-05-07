def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1<<26):
        cnt = 0
        for s in S:
            tmp = 0
            for j in range(26):
                if i>>j & 1:
                    tmp |= 1<<ord(s[j])-97
            if bin(tmp).count("1") == K:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
