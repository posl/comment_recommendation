def main():
    S = input()
    N = len(S)
    ans = [1] * N
    l = 0
    r = 0
    for i in range(N):
        if S[i] == 'L':
            l = i
        else:
            r = i
        if l != r:
            ans[l] += ans[r]
            ans[r] = 0
    print(*ans)
