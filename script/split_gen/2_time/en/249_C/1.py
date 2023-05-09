def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    alphabets = set()
    for s in S:
        alphabets = alphabets | set(s)
    ans = 0
    for i in range(1, 2**N):
        s = set()
        for j in range(N):
            if (i >> j) & 1:
                s = s | set(S[j])
        if len(s) == K:
            ans = max(ans, len(alphabets & s))
    print(ans)
