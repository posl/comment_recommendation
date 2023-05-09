def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "R":
            ans += 1
            break
    for i in range(N-1, -1, -1):
        if S[i] == "L":
            ans += 1
            break
    ans += 2 * min(K, S.count("RL"))
    print(min(ans, N))
