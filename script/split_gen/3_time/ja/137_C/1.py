def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if len(S[i]) != len(S[j]):
                break
            if sorted(S[i]) == sorted(S[j]):
                ans += 1
    print(ans)
