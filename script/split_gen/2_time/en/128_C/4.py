def main():
    N, M = map(int, input().split())
    S = []
    P = []
    for _ in range(M):
        s = list(map(int, input().split()))
        S.append(s[1:])
        P.append(int(input()))
    ans = 0
    for i in range(2**N):
        f = True
        for j in range(M):
            if P[j] != sum([i >> (s-1) & 1 for s in S[j]]) % 2:
                f = False
                break
        if f:
            ans += 1
    print(ans)
