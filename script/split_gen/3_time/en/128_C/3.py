def main():
    N, M = map(int, input().split())
    S = [[int(i) for i in input().split()] for _ in range(M)]
    P = [int(i) for i in input().split()]
    ans = 0
    for i in range(2**N):
        for j in range(M):
            if P[j] != sum([i >> (s-1) & 1 for s in S[j][1:]]) & 1:
                break
        else:
            ans += 1
    print(ans)
