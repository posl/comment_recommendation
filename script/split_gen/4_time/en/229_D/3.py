def solve():
    S = input()
    K = int(input())
    N = len(S)
    ans = 0
    cnt = 0
    for i in range(N):
        if S[i] == "X":
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    if ans + K >= N:
        print(N)
    else:
        print(ans + K + 1)
