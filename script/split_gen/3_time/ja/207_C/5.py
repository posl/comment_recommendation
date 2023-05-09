def main():
    N = int(input())
    S = []
    for _ in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            S.append((l, r))
        elif t == 2:
            S.append((l, r - 1))
        elif t == 3:
            S.append((l + 1, r))
        else:
            S.append((l + 1, r - 1))
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if S[i][0] <= S[j][1] and S[j][0] <= S[i][1]:
                ans += 1
    print(ans)
