def main():
    N, K = map(int, input().split())
    S = [input() for i in range(N)]
    ans = 0
    for i in range(2 ** 26):
        cnt = 0
        for j in range(N):
            tmp = 0
            for k in S[j]:
                if i >> (ord(k) - ord('a')) & 1:
                    tmp += 1
            if tmp >= K:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
