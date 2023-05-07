def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1, N):
        for j in range(i+1, N+1):
            if "o" not in S[i-1] and "o" not in S[j-1]:
                continue
            else:
                ans += 1
    print(ans)
