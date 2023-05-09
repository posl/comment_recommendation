def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1 << 26):
        cnt = 0
        for s in S:
            mask = 0
            for c in s:
                mask |= 1 << (ord(c) - ord('a'))
            if bin(mask & i).count('1') >= K:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
