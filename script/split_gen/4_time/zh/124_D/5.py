def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for l in range(N):
        for r in range(l, N):
            if S[r] == "0":
                K -= 1
            if K < 0:
                if S[l] == "0":
                    K += 1
                break
            ans = max(ans, r - l + 1)
    print(ans)
