def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1<<N):
        l = []
        for j in range(N):
            if i & 1<<j:
                l.append(S[j])
        if len(l) == K:
            ans = max(ans, len(set(''.join(l))))
    print(ans)
