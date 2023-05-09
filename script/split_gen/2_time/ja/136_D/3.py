def main():
    S = input()
    N = len(S)
    ans = [0] * N
    ans[0] = 1
    ans[N-1] = 1
    for i in range(1, N):
        if S[i] == 'R' and S[i-1] == 'L':
            ans[i] += ans[i-1]
            ans[i-1] = 0
        else:
            ans[i] += ans[i-1]
    for i in range(N-1, 0, -1):
        if S[i] == 'L' and S[i-1] == 'R':
            ans[i-1] += ans[i]
            ans[i] = 0
        else:
            ans[i-1] += ans[i]
    print(*ans)
